import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from datetime import timedelta
from .db.sales import get_list_of_sales
from .db.days import get_list_of_days
from .const import time_steps

def get_output_scaler(user_name, product):
		output_scaler = MinMaxScaler()

		sales_counts_per_hour = get_sales_count_per_product(user_name, product)
		output_scaler.fit(sales_counts_per_hour)
		
		return output_scaler

def get_output_data(user_name, product):
    sales_counts_per_hour = get_sales_count_per_product(user_name, product)
    normalize_output_data = get_normalize_output_data(sales_counts_per_hour)
    reshape_output_data = get_reshape_output_data(normalize_output_data)
    
    return reshape_output_data

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
  
def get_normalize_output_data(output_data):
		output_scaler = MinMaxScaler()

		return output_scaler.fit_transform(output_data)

def get_reshape_output_data(output_data):
    output_data = np.array(output_data)
    
    output_data_reshaped = []
    for i in range(0, len(output_data) - time_steps + 1, time_steps):
        output_data_reshaped.append(output_data[i:i + time_steps])

    return np.array(output_data_reshaped)
