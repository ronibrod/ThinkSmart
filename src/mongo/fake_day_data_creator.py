import math
import random
from datetime import timedelta

days_in_year = 365
base_temp = 25
temp_amplitude = 16
noise_strength = 3

def create_days_array(start_date, end_date):
  date_array = []
  current_date = start_date
  day_counter = 1
  
  
  while current_date <= end_date:
    date_str = current_date.strftime('%d/%m/%Y')
    day_of_week = current_date.weekday()  # Monday is 0 and Sunday is 6
    temperature = round(base_temp + temp_amplitude * math.sin(2 * math.pi * (day_counter % days_in_year) / days_in_year) + random.randint(0, noise_strength))
    rain = get_rain_data(day_counter)
    events = get_events_data(current_date)
    
    date_array.append({
      'date_id': 'date_id_' + date_str,
      'date': current_date,
      'day_of_week': ((day_of_week + 1) % 7) + 1,
      'temperature': temperature,
      'rain': rain,
      'events': events,
    })
    
    day_counter += 1
    current_date += timedelta(days=1)
  
  return date_array

def get_rain_data(day_counter):
  percent_for_rain = round(math.sin(2 * math.pi * (day_counter % days_in_year) / days_in_year) * 50) + 100
  random_number_for_percent_rain = random.randint(0, 100)
  rain = 0
  
  if random_number_for_percent_rain > percent_for_rain:
    rain = math.sqrt((random_number_for_percent_rain - percent_for_rain) / 50)
    
  return rain

def get_events_data(current_date):
  events = {}
  if current_date.month  in [7, 8]:
    events['vacation'] = 1
  else:
    events['vacation'] = 0

  events['holiday'] = 0
  events['unusual'] = 0
    
  return events
