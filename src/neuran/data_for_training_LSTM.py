import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from datetime import timedelta
from .db.sales import get_list_of_sales
from .db.days import get_list_of_days

def get_sales_count_per_product(user_name, product):
    list_of_sales = get_list_of_sales(user_name, product)
    list_of_days = get_list_of_days(user_name)
    
    sales_counts_per_hour = []
    
    for day in list_of_days:
        if day is not None:
            date = day['date']

            hourly_counts = [0] * 24  # Initialize a list of 24 zeros for the 24 hours of the day
            for sale in list_of_sales:
                if date <= sale['date'] < date + timedelta(days=1):
                    hour = sale['date'].hour
                    hourly_counts[hour] += 1
            sales_counts_per_hour.append(hourly_counts)

    return sales_counts_per_hour

def get_input_data_per_day(user_name):
    list_of_days = get_list_of_days(user_name)
    
    input_data_per_hour = []
    
    for day in list_of_days:
        if day is not None:
            day_data = [
                day['date'].year,
                day['date'].month,
                ((day['date'].weekday() + 1) % 7) + 1,  # Adjusted day of the week (1-7)
                day['temperature'],
                day['rain'],
                day['events'][0] if len(day['events']) > 0 else 'none',
                day['events'][1] if len(day['events']) > 1 else 'none',
                day['events'][2] if len(day['events']) > 2 else 'none',
            ]
            input_data_per_hour.append(day_data)

    return input_data_per_hour
  
def build_input_data(date_data_per_day, time_steps=7, input_features=7):
    # Initialize empty array for input data
    input_data = []
    
    # Iterate through each day data dictionary in date_data_per_day
    for day_data_dict in date_data_per_day:
        day_data = day_data_dict['day_data']
        input_data.append([
            day_data['year'],
            day_data['month'],
            day_data['temperature'],
            day_data['rain'],
            day_data['event1'],
            day_data['event2'],
            day_data['event3']
        ])
    
    # Convert input_data to a numpy array
    input_data = np.array(input_data)
    
    # Reshape input_data into array of arrays with time_steps and input_features dimensions
    input_data_reshaped = []
    for i in range(0, len(input_data) - time_steps + 1, time_steps):
        input_data_reshaped.append(input_data[i:i + time_steps])

    return np.array(input_data_reshaped)

# Example usage:
date_data_per_day = get_date_data_per_day()
input_data = build_input_data(date_data_per_day)
print('ttt', len(input_data))

def build_output_data(output_data, time_steps=7, output_features=24):
    output_data = np.array(output_data)
    
    output_data_reshaped = []
    for i in range(0, len(output_data) - time_steps + 1, time_steps):
        output_data_reshaped.append(output_data[i:i + time_steps])

    return np.array(output_data_reshaped)


def normalize_input_data(input_data):
    # Initialize the scaler and label encoders
    scaler = MinMaxScaler()
    label_encoders = [LabelEncoder() for _ in range(3)]  # Assuming 3 categorical features

    # Flatten the input_data to 2D for the scaler
    n_samples, n_time_steps, n_features = input_data.shape
    input_data_reshaped = input_data.reshape(-1, n_features)
    
    # Separate numeric and categorical data
    numeric_data = input_data_reshaped[:, :4].astype(float)  # Assuming the first 4 features are numeric
    categorical_data = input_data_reshaped[:, 4:]  # The last 3 features are categorical

    # Normalize numeric data
    numeric_data_normalized = scaler.fit_transform(numeric_data)

    # Encode categorical data
    for i in range(categorical_data.shape[1]):
        categorical_data[:, i] = label_encoders[i].fit_transform(categorical_data[:, i])

    # Combine numeric and encoded categorical data
    input_data_normalized_reshaped = np.hstack((numeric_data_normalized, categorical_data))

    # Reshape back to the original shape
    input_data_normalized = input_data_normalized_reshaped.reshape(n_samples, n_time_steps, n_features)

    return input_data_normalized, scaler, label_encoders
  
input_data_normalized, scaler, label_encoders = normalize_input_data(input_data)
print("Shape of input_data array:", input_data.shape)
print("Shape of normalized input_data array:", input_data_normalized.shape)


def normalize_output_data(output_data):
    scaler = MinMaxScaler()
    
    # Reshape 3D array to 2D
    n_samples, n_time_steps, n_features = output_data.shape
    output_data_reshaped = output_data.reshape(-1, n_features)
    
    # Apply the scaler
    scaled_data = scaler.fit_transform(output_data_reshaped)
    
    # Reshape back to 3D
    output_data_normalized = scaled_data.reshape(n_samples, n_time_steps, n_features)
    
    return output_data_normalized, scaler

# Example usage:
output_data = get_sales_count_per_day()
output_data_reshaped = build_output_data(output_data)
output_data_normalized, scaler = normalize_output_data(output_data_reshaped)

# Print shape of output_data array
print("Shape of output_data array:", len(output_data))
print("Shape of normalized output_data array:", output_data_normalized.shape)
# print(output_scaler.shape)

def get_training_data():
    return input_data_normalized, output_data_normalized, scaler
  


# def get_training_data():
#     # Fetch the input and output data
#     date_data_per_day = get_date_data_per_day()
#     sales_count_per_day = get_sales_count_per_day()

#     # Ensure that both datasets cover the same time range and intervals
#     sales_count_per_day_dict = {item['date']: item['count'] for item in sales_count_per_day}

#     # Label encoding for categorical variables
#     label_encoder = LabelEncoder()

#     # Extract relevant features and encode categorical variables
    # features = ['temperature', 'rain', 'event1', 'event2', 'event3', 'year', 'month']

    # data = []
    # output_data = []

    # for item in date_data_per_day:
    #     day_data = item['day_data']
    #     day = item['day']
    #     if day in sales_count_per_day_dict:
    #         # Encode categorical events
    #         event1_encoded = label_encoder.fit_transform([day_data['event1']])[0]
    #         event2_encoded = label_encoder.fit_transform([day_data['event2']])[0]
    #         event3_encoded = label_encoder.fit_transform([day_data['event3']])[0]
            
    #         data_point = [
    #             day_data['temperature'],
    #             day_data['rain'],
    #             event1_encoded,
    #             event2_encoded,
    #             event3_encoded,
    #             day_data['year'],
    #             day_data['month']
    #         ]
    #         data.append(data_point)
    #         output_data.append(sales_count_per_day_dict[day])
            
#     # Convert data to numpy array for further processing
#     data = np.array(data)
#     output_data = np.array(output_data).reshape(-1, 1)

#     # Normalize numerical features (temperature, rain, etc.)
#     scaler = MinMaxScaler()
#     data[:, 0:2] = scaler.fit_transform(data[:, 0:2])

#     # Normalize categorical features separately (if required)
#     categorical_columns = [2, 3, 4]
#     for col in categorical_columns:
#         max_value = np.max(data[:, col])
#         if max_value != 0:
#             data[:, col] = data[:, col] / max_value

#     # Define constants for timesteps and features
#     num_samples = len(data)
#     num_days_per_week = 7  # Days per week
#     num_features = len(features)

#     # Prepare the input data for LSTM model
#     input_data = np.zeros((num_samples, num_days_per_week, num_features))

#     for i in range(num_samples):
#         day_data = date_data_per_day[i]['day_data']
#         day_index = day_data['day_of_week'] - 1  # Adjusting to 0-based index (0-6)
#         input_data[i, day_index, :] = data[i, :]

#     # Reshape the output data to match the number of samples and days per week
#     output_data = output_data.reshape(num_samples, 1)

#     # Normalize the output data (sales count) to be between 0 and 1
#     output_scaler = MinMaxScaler()
#     output_data = output_scaler.fit_transform(output_data)

#     return input_data, output_data, output_scaler
