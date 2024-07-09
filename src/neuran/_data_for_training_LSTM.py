import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from pymongo import MongoClient
from datetime import datetime, timedelta

def get_sales_collection():
    client = MongoClient('localhost', 27017)
    db = client['lizCafeteria']
    sales_collection = db['sale']
    return sales_collection

def get_days_collection():
    client = MongoClient('localhost', 27017)
    db = client['lizCafeteria']
    days_collection = db['day']
    return days_collection

def get_first_and_last_sale_dates():
    sales_collection = get_sales_collection()
    first_sale = sales_collection.find_one({}, sort=[('date', 1)])  # Ascending order for the first sale
    last_sale = sales_collection.find_one({}, sort=[('date', -1)])  # Descending order for the last sale
    
    if first_sale and last_sale:
        return first_sale['date'], last_sale['date']
    else:
        return None, None

def get_sales_count_per_hour():
    sales_collection = get_sales_collection()
    first_date, last_date = get_first_and_last_sale_dates()
    
    if not first_date or not last_date:
        return []
    
    query = {
      'date': {'$gte': first_date, '$lte': last_date},
      'product': 'Espresso',
    }
    all_sales = list(sales_collection.find(query))
    
    sales_per_hour = {}
    
    current_date = first_date.replace(minute=0, second=0, microsecond=0)
    end_date = last_date.replace(minute=0, second=0, microsecond=0)
    
    while current_date <= end_date:
        next_hour = current_date + timedelta(hours=1)
        count = sum(1 for sale in all_sales if current_date <= sale['date'] < next_hour)
        sales_per_hour[current_date] = count
        current_date = next_hour
    
    result = [{'date': date, 'count': sales_per_hour[date]} for date in sales_per_hour]
    return result

def get_date_data_per_hour():
    days_collection = get_days_collection()
    first_date, last_date = get_first_and_last_sale_dates()
    
    if not first_date or not last_date:
        return []
    
    query = {'date': {'$gte': first_date, '$lte': last_date}}
    all_days = list(days_collection.find(query))
    
    date_data_per_hour = {}
    
    current_hour = first_date.replace(minute=0, second=0, microsecond=0)
    end_hour = last_date.replace(minute=0, second=0, microsecond=0)
    
    while current_hour <= end_hour:
        day = next((day for day in all_days if day['date'].date() == current_hour.date()), None)
        
        if day is not None:
            hour_data = {
                'year': day['date'].year,
                'month': day['date'].month,
                'day_of_week': ((day['date'].weekday() + 1) % 7) + 1,  # Adjusted day of the week (1-7)
                'hour': current_hour.hour,
                'temperature': day['temperature'],
                'rain': day['rain'],
                'event1': day['events'][0] if len(day['events']) > 0 else 'none',
                'event2': day['events'][1] if len(day['events']) > 1 else 'none',
                'event3': day['events'][2] if len(day['events']) > 2 else 'none',
            }
            date_data_per_hour[current_hour] = hour_data
        
        current_hour = current_hour + timedelta(hours=1)
    
    result = [{'hour': hour, 'hour_data': date_data_per_hour[hour]} for hour in date_data_per_hour]
    return result

def get_training_data():
  # Fetch the input and output data
  date_data_per_hour = get_date_data_per_hour()
  print('Got date_data_per_hour, len:', len(date_data_per_hour))
  sales_count_per_hour = get_sales_count_per_hour()
  print('Got sales_count_per_hour, len:', len(sales_count_per_hour))

  # Ensure that both datasets cover the same time range and intervals
  sales_count_per_hour_dict = {item['date']: item['count'] for item in sales_count_per_hour}

  # Label encoding for categorical variables
  label_encoder = LabelEncoder()

  # Extract relevant features and encode categorical variables
  features = ['temperature', 'rain', 'event1', 'event2', 'event3', 'year', 'month']

  data = []
  output_data = []

  for item in date_data_per_hour:
      hour_data = item['hour_data']
      hour = item['hour']
      if hour in sales_count_per_hour_dict:
          # Encode categorical events
          event1_encoded = label_encoder.fit_transform([hour_data['event1']])[0]
          event2_encoded = label_encoder.fit_transform([hour_data['event2']])[0]
          event3_encoded = label_encoder.fit_transform([hour_data['event3']])[0]
          
          data_point = [
              hour_data['temperature'],
              hour_data['rain'],
              event1_encoded,
              event2_encoded,
              event3_encoded,
              hour_data['year'],
              hour_data['month']
          ]
          data.append(data_point)
          output_data.append(sales_count_per_hour_dict[hour])
          
  print('Created data and output_data')

  # Convert data to numpy array for further processing
  data = np.array(data)
  output_data = np.array(output_data).reshape(-1, 1)

  # Normalize numerical features (temperature, rain, etc.)
  scaler = MinMaxScaler()
  data[:, 0:2] = scaler.fit_transform(data[:, 0:2])

  # Normalize categorical features separately (if required)
  categorical_columns = [2, 3, 4]
  for col in categorical_columns:
      max_value = np.max(data[:, col])
      if max_value != 0:
          data[:, col] = data[:, col] / max_value

  # Define constants for timesteps and features
  num_samples = len(data)
  num_days_per_week = 7  # Days per week
  num_hours_per_day = 24  # Hours per day
  num_features = len(features)

  # Prepare the input data for LSTM model
  input_data = np.zeros((num_samples, num_days_per_week, num_hours_per_day, num_features))

  for i in range(num_samples):
      if i % 10000 == 0:
          print(f'Processing sample {i}')
      
      hour_data = date_data_per_hour[i]['hour_data']
      day_index = hour_data['day_of_week'] - 1  # Adjusting to 0-based index (0-6)
      hour_index = hour_data['hour']  # 0-23
      input_data[i, day_index, hour_index, :] = data[i, :]

  # Print the constructed input data for one example (first sample)
  print("Constructed Input Data:")
  # print(input_data[0][:10])  # Displaying data for the first sample

  # Normalize the output data (sales count) to be between 0 and 1
  output_scaler = MinMaxScaler()
  output_data = output_scaler.fit_transform(output_data)

  # Print the output data
  print("Constructed Output Data:")
  # print(output_data[:10])  # Displaying first 10 output data points

  return input_data, output_data, output_scaler
