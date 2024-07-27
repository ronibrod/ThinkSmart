import math
import random
from datetime import timedelta
from ..parse.temperature_xl import get_temperature_data
from ..parse.rain_xl import get_rain_data

days_in_year = 365
base_temp = 25
temp_amplitude = 16
noise_strength = 3

def create_days_array(start_date, end_date):
	temperature_data = get_temperature_data()
	rain_data = get_rain_data()
	
	date_array = []
	day_index = 0
	
	current_date = start_date
	while current_date <= end_date:
		date_str = current_date.strftime('%d/%m/%Y')
		day_of_week = ((current_date.weekday() + 1) % 7) + 1
		temperature = temperature_data[day_index]
		rain = rain_data[day_index]['rain']
		events = get_events_data(current_date)
		total_sales = create_total_number_of_sales(current_date, day_of_week, temperature, rain, events)
		
		date_array.append({
		'date_id': 'date_id_' + date_str,
		'date': current_date,
		'day_of_week': day_of_week,
		'min_temperature': temperature['min'] if temperature['min'] else None,
    'max_temperature': temperature['max'] if temperature['max'] else None,
		'rain': rain,
		'events': events,
  	'total_sales': int(total_sales),
		})
		
		day_index += 1
		current_date += timedelta(days=1)
	
	return date_array

def get_events_data(current_date):
  events = {}
  if current_date.month  in [7, 8]:
    events['vacation'] = 1
  else:
    events['vacation'] = 0

  events['holiday'] = 0
  events['unusual'] = 0
    
  return events

def create_total_number_of_sales(date, day_of_week, temperature, rain, events):
  base_num = 200  # base
  temperature = None
  try:
    temperature = abs(round(((temperature['max'] * 3) + temperature['min']) / 4))
  except Exception as e:
    temperature = 30
    
  number_of_sales = random.uniform(base_num * 0.85, base_num * 1.15) # base random
  if day_of_week in range(1, 5):
    number_of_sales *= random.uniform(1.1, 1.15)
  elif day_of_week in range(5, 7):
    number_of_sales *= random.uniform(0.85, 0.9)
  else:
    number_of_sales *= random.uniform(0.7, 0.8)
    
  month = date.month
  day_of_month = date.day
    
  if month in range(2, 5):
    base_for_season = 0.8
    base_for_season += ((((month - 2) * 30) + day_of_month) / 3.6) / 100
    number_of_sales *= random.uniform(base_for_season, base_for_season + 0.1)
  elif month in range(5, 8):
    base_for_season = 1.05
    base_for_season += ((((month - 5) * 30) + day_of_month) / 9) / 100
    number_of_sales *= random.uniform(base_for_season, base_for_season + 0.1)
  elif month in range(8, 11):
    base_for_season = 1.15
    base_for_season -= ((((month - 8) * 30) + day_of_month) / 3) / 100
    number_of_sales *= random.uniform(base_for_season, base_for_season + 0.1)
  else:
    month = 13 if month == 1 else month
    base_for_season = 0.95
    base_for_season -= ((((month - 11) * 30) + day_of_month) / 18) / 100
    number_of_sales *= random.uniform(base_for_season, base_for_season + 0.1)
    
  if temperature <= 0:
    base_for_temp = 0.7
    base_for_temp += ((temperature) / 1) / 100
    number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
  elif temperature in range(1, 11):
    base_for_temp = 0.7
    base_for_temp += ((temperature - 11) / 0.28) / 100
    number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
  elif temperature in range(11, 21):
    base_for_temp = 1.05
    base_for_temp += ((temperature - 11) / 1) / 100
    number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
  elif temperature in range(21, 31):
    base_for_temp = 1.15
    base_for_temp += ((temperature - 21) / 1) / 100
    number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
  elif temperature in range(31, 36):
    base_for_temp = 1.25
    base_for_temp += ((temperature - 31) / 0.5) / 100
    number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
  elif temperature in range(36, 41):
    base_for_temp = 1.35
    base_for_temp -= ((temperature - 36) / 0.5) / 100
    number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
  elif temperature >= 41:
    base_for_temp = 1.25
    base_for_temp -= ((temperature - 41) / 0.2) / 100
    number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
    
  if 0 < rain < 1:
    base_for_rain = 0.9
    number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
  elif rain in range(1, 11):
    base_for_rain = 0.9
    base_for_rain -= ((rain - 1) / 1) / 100
    number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
  elif rain in range(11, 31):
    base_for_rain = 0.8
    base_for_rain -= ((rain - 11) / 2) / 100
    number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
  elif 31 <= rain <= 50:
    base_for_rain = 0.7
    number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
  elif rain > 50:
    base_for_rain = 0.6
    number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
    
  if events['vacation'] == 1:
    base_for_vacation = 1.05
    number_of_sales *= random.uniform(base_for_vacation, base_for_vacation + 0.1)
  if events['unusual'] != 0:
    base_for_unusual_events += events['unusual'] * number_of_sales
    number_of_sales += random.uniform(base_for_unusual_events, base_for_unusual_events + 0.2)

  if number_of_sales > 400:
    print(number_of_sales, temperature, month)
  return number_of_sales
