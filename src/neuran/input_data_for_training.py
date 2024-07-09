import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from .db.days import get_list_of_days
from .const import time_steps

def get_input_data(user_name):
    input_data_per_hour = get_input_data_per_day(user_name)
    normalize_input_data = get_normalize_input_data(input_data_per_hour)
    reshape_input_data = get_reshape_input_data(normalize_input_data)
    
    return reshape_input_data

def get_input_data_per_day(user_name):
    list_of_days = get_list_of_days(user_name)
    
    input_data_per_hour = []
    
    for day in list_of_days:
        if day is not None:
            day_data = [
                day['date'].year,
                day['date'].month,
                day['temperature'],
                day['rain'],
                day['events']['vacation'],
                day['events']['holiday'],
                day['events']['unusual'],
            ]
            input_data_per_hour.append(day_data)

    return input_data_per_hour
  
def get_normalize_input_data(input_data):
    scaler = MinMaxScaler()
    
    return scaler.fit_transform(input_data) 

def get_reshape_input_data(input_data):
    input_data = np.array(input_data)
    
    input_data_reshaped = []
    for i in range(0, len(input_data) - time_steps + 1, time_steps):
        input_data_reshaped.append(input_data[i:i + time_steps])

    return np.array(input_data_reshaped)

