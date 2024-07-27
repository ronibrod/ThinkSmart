# import math
import random
# from .fake_day_data_creator import create_days_array
# from .fake_product_data_creator import create_products_array

num_of_categories = 4

def create_sales_array(days, products):
  salse_array = []
  # list_of_days = create_days_array(start_date, end_date)
  # list_of_products = create_products_array()
  # list_of_days = get_days_array(start_date, end_date)
  # list_of_products = get_products_array()
  products_by_category = get_products_by_category(products)
  list_of_categories = list(products_by_category.keys())

  for day in days:
    number_of_sales = day['total_sales']

    for sale in range(1, int(number_of_sales) + 1):
      random_hour = get_random_hour()
      random_minute = random.randint(0, 59)
      random_second = random.randint(0, 59)
      time = day['date']
      time = time.replace(hour=random_hour, minute=random_minute, second=random_second)
      
      random_number_of_category = get_random_number_of_category(day, random_hour)
      random_number_of_product = get_random_number_of_product(random_number_of_category)
      # random_number_of_category = create_random_number_of_category(random_hour, day)
      # random_number_of_category = random.randint(0, len(list_of_categories) - 1)
      # random_number_of_product = random.randint(0, len(products_by_category[list_of_categories[random_number_of_category]]) - 1)
      
      salse_array.append({
        'sale_id': f'{sale}' + '_' + time.strftime('%d/%m/%Y_%H:%M:%S') + '_' + products[random_number_of_product]['name'],
        'product': products_by_category[list_of_categories[random_number_of_category]][random_number_of_product]['name'],
        'category': products_by_category[list_of_categories[random_number_of_category]][random_number_of_product]['category'],
        'date': time,
        'year': time.year,
        'month': time.month,
        'day_of_month': time.day,
        'day_of_week': time.weekday(),
        'hour': time.hour,
      })

  return salse_array

def get_products_by_category(list_of_products):
  products_by_category = {}
  
  for product in list_of_products:
    category = product['category']
    
    if category not in products_by_category:
      products_by_category[product['category']] = []
      
    products_by_category[product['category']].append(product)

  return products_by_category

# def get_number_of_sales(day):
#   base_num = 200  # base
#   temperature = None
#   try:
#     temperature = abs(round(((day['max_temperature'] * 3) + day['min_temperature']) / 4))
#   except Exception as e:
#     temperature = 30
    
#   number_of_sales = random.uniform(base_num * 0.85, base_num * 1.15) # base random
#   if day['day_of_week'] in range(1, 5):
#     number_of_sales *= random.uniform(1.1, 1.15)
#   elif day['day_of_week'] in range(5, 7):
#     number_of_sales *= random.uniform(0.85, 0.9)
#   else:
#     number_of_sales *= random.uniform(0.7, 0.8)
    
#   month = day['date'].month
#   day_of_month = day['date'].day
    
#   if month in range(2, 5):
#     base_for_season = 0.8
#     base_for_season += ((((month - 2) * 30) + day_of_month) / 3.6) / 100
#     number_of_sales *= random.uniform(base_for_season, base_for_season + 0.1)
#   elif month in range(5, 8):
#     base_for_season = 1.05
#     base_for_season += ((((month - 5) * 30) + day_of_month) / 9) / 100
#     number_of_sales *= random.uniform(base_for_season, base_for_season + 0.1)
#   elif month in range(8, 11):
#     base_for_season = 1.15
#     base_for_season -= ((((month - 8) * 30) + day_of_month) / 3) / 100
#     number_of_sales *= random.uniform(base_for_season, base_for_season + 0.1)
#   else:
#     month = 13 if month == 1 else month
#     base_for_season = 0.95
#     base_for_season -= ((((month - 11) * 30) + day_of_month) / 18) / 100
#     number_of_sales *= random.uniform(base_for_season, base_for_season + 0.1)
    
#   # print(temperature)
#   # if month == 8:
#   #   print(number_of_sales, temperature)
    
#   if temperature <= 0:
#     base_for_temp = 0.7
#     base_for_temp += ((temperature) / 1) / 100
#     number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
#   elif temperature in range(1, 11):
#     base_for_temp = 0.7
#     base_for_temp += ((temperature - 11) / 0.28) / 100
#     number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
#   elif temperature in range(11, 21):
#     base_for_temp = 1.05
#     base_for_temp += ((temperature - 11) / 1) / 100
#     number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
#   elif temperature in range(21, 31):
#     base_for_temp = 1.15
#     base_for_temp += ((temperature - 21) / 1) / 100
#     number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
#   elif temperature in range(31, 36):
#     base_for_temp = 1.25
#     base_for_temp += ((temperature - 31) / 0.5) / 100
#     number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
#   elif temperature in range(36, 41):
#     base_for_temp = 1.35
#     base_for_temp -= ((temperature - 36) / 0.5) / 100
#     number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
#   elif temperature >= 41:
#     base_for_temp = 1.25
#     base_for_temp -= ((temperature - 41) / 0.2) / 100
#     number_of_sales *= random.uniform(base_for_temp, base_for_temp + 0.05)
    
#   # if month == 8:
#   #   print(number_of_sales)
    
#   if 0 < day['rain'] < 1:
#     base_for_rain = 0.9
#     number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
#   elif day['rain'] in range(1, 11):
#     base_for_rain = 0.9
#     base_for_rain -= ((day['rain'] - 1) / 1) / 100
#     number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
#   elif day['rain'] in range(11, 31):
#     base_for_rain = 0.8
#     base_for_rain -= ((day['rain'] - 11) / 2) / 100
#     number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
#   elif 31 <= day['rain'] <= 50:
#     base_for_rain = 0.7
#     number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
#   elif day['rain'] > 50:
#     base_for_rain = 0.6
#     number_of_sales *= random.uniform(base_for_rain, base_for_rain + 0.1)
    
#   if day['events']['vacation'] == 1:
#     base_for_vacation = 1.05
#     number_of_sales *= random.uniform(base_for_vacation, base_for_vacation + 0.1)
#   if day['events']['unusual'] != 0:
#     base_for_unusual_events += day['events']['unusual'] * number_of_sales
#     number_of_sales += random.uniform(base_for_unusual_events, base_for_unusual_events + 0.2)

#   if number_of_sales > 400:
#     print(number_of_sales, temperature, month)
#   return number_of_sales

def get_random_hour():
  morning = random.randint(20, 25)
  afternoon = random.randint(20, 25)
  evening = random.randint(15, 20)
  night = random.randint(25, 30)
  
  all_day = morning + afternoon + evening + night
  
  period_of_day = random.randint(1, all_day)
  if period_of_day <= morning:
    return random.randint(8, 11)
  
  period_of_day -= morning
  if period_of_day <= afternoon:
    return random.randint(12, 15)
  
  period_of_day -= afternoon
  if period_of_day <= evening:
    return random.randint(16, 19)
  
  return random.randint(20, 23)
    
def get_random_number_of_category(day, random_hour):
  temperature = None
  try:
    temperature = abs(round((day['max_temperature'] * 2) + day['min_temperature'] / 3))
  except Exception as e:
    temperature = 30
  
  category1 = random.uniform(35, 45) # 40
  category2 = random.uniform(20, 30) # 25
  category3 = random.uniform(10, 20) # 15
  category4 = random.uniform(15, 25) # 20
    
  base_for_categories = []
  categories_division = []
  temp_influence = None
    
  if temperature <= 0:
    base_for_categories = [20, -10, -5, -5]
    categories_division = [0, 0, 0, 0]
    temp_influence = temperature
  elif temperature in range(1, 11):
    base_for_categories = [20, -10, -5, -5]
    categories_division = [-1, 0.5, 0, 0.5]
    temp_influence = temperature - 1
  elif temperature in range(11, 21):
    base_for_categories = [10, -5, -5, 0]
    categories_division = [-2, 1, 1, 0]
    temp_influence = temperature - 11
  elif temperature in range(21, 31):
    base_for_categories = [-10, 5, 5, 0]
    categories_division = [-1, 1, 0, 0]
    temp_influence = temperature - 21
  elif temperature in range(31, 41):
    base_for_categories = [-20, 15, 5, 0]
    categories_division = [-1, 1, 0, 0]
    temp_influence = temperature - 31
  elif temperature >= 41:
    base_for_categories = [-30, 25, 5, 0]
    categories_division = [0, 0, 0, 0]
    temp_influence = temperature - 41
    
  c1, c2, c3, c4 = get_categories_by_temp(temp_influence, base_for_categories, categories_division)
  category1 += c1
  category2 += c2
  category3 += c3
  category4 += c4

  if day['day_of_week'] in range(1, 3):
    category1 *= random.uniform(0.9, 0.95)
    category2 *= random.uniform(1.05, 1.1)
    category3 *= random.uniform(0.9, 0.95)
    category4 *= random.uniform(0.9, 0.95)
  elif day['day_of_week'] in range(3, 5):
    category1 *= random.uniform(0.9, 0.95)
    category2 *= random.uniform(1.1, 1.15)
    category3 *= random.uniform(0.9, 0.95)
    category4 *= random.uniform(0.9, 0.95)
  elif day['day_of_week'] in range(5, 7):
    category1 *= random.uniform(0.85, 0.9)
    category2 *= random.uniform(0.85, 0.9)
    category3 *= random.uniform(1.1, 1.15)
    category4 *= random.uniform(1.15, 1.2)
  else:
    category1 *= random.uniform(0.9, 0.95)
    category2 *= random.uniform(1.05, 1.1)
    category3 *= random.uniform(0.9, 0.95)
    category4 *= random.uniform(0.9, 0.95)

  if random_hour < 12:
    category1 *= random.uniform(1.45, 1.55) # 60
    category2 *= random.uniform(0.35, 0.45) # 10
    category3 *= random.uniform(1.6, 1.7) # 25
    category4 *= random.uniform(0.2, 0.3) # 5
  elif 12 <= random_hour < 16:
    category1 *= random.uniform(0.55, 0.65) # 25
    category2 *= random.uniform(1.55, 1.65) # 40
    category3 *= random.uniform(1.6, 1.7) # 25
    category4 *= random.uniform(0.45, 0.55) # 10
  elif 16 <= random_hour < 20:
    category1 *= random.uniform(0.45, 0.55) # 20
    category2 *= random.uniform(0.95, 1.05) # 25
    category3 *= random.uniform(1.6, 1.7) # 25
    category4 *= random.uniform(1.45, 0.55) # 30
  else:
    category1 *= random.uniform(0.2, 0.3) # 10
    category2 *= random.uniform(0.15, 0.25) # 5
    category3 *= random.uniform(1.6, 1.7) # 25
    category4 *= random.uniform(2.9, 3.1) # 60
  
  all_categories = category1 + category2 + category3 + category4
  chosen_category = random.uniform(1, all_categories)
  if chosen_category <= category1:
    return 0
  
  chosen_category -= category1
  if chosen_category <= category2:
    return 1
  
  chosen_category -= category2
  if chosen_category <= category3:
    return 2
  
  return 3
  
def get_categories_by_temp(temp_influence, base_for_categories, categories_division):
  categories_values = []
  for index in range(0, num_of_categories):
    base = base_for_categories[index]
    if categories_division[index] != 0:
      base += (temp_influence / categories_division[index])
      
    categories_values.append(random.uniform(base - 5, base + 5))
    
  return categories_values
  
def get_random_number_of_product(category):
  products_chance = []
  if category == 0:
    products_chance = [3, 3, 1, 1, 1, 1]
  if category == 1:
    products_chance = [3, 3, 3, 2, 1, 1, 2]
  if category == 2:
    products_chance = [3, 3, 1, 2, 1]
  if category == 3:
    products_chance = [3, 3, 2]
  
  randum_num = random.randint(1, sum(products_chance))
  
  for index, product in enumerate(products_chance):
    if randum_num <= product:
      return index
    randum_num -= product
  
  return 0
    
    
    
    
    
  
  
  
  
  # day_of_week_effect = round(math.sin(math.pi * (((day['day_of_week'] + 6) % 8) / 8))) # add by day of week
  # day_of_week_effect += random.randint(round(day_of_week_effect * 20), round(day_of_week_effect * 50))
  
  # min_temerature_effect = round(6 - abs(temperature - 30))
  # max_temerature_effect = round(random.randint(1, 20) + (min_temerature_effect * 2))
  # if min_temerature_effect > max_temerature_effect:
  #   min_temerature_effect, max_temerature_effect = max_temerature_effect, min_temerature_effect
  # elif min_temerature_effect == max_temerature_effect:
  #   max_temerature_effect += 1

  # temerature_effect = random.randint(min_temerature_effect, max_temerature_effect)
  
  # min_rain_effect = round((1 - day['rain']) - 1 ** 3)* 20
  # max_rain_effect = min_rain_effect * 5
  # if min_rain_effect > max_rain_effect:
  #   min_rain_effect, max_rain_effect = max_rain_effect, min_rain_effect
  # elif min_rain_effect == max_rain_effect:
  #   max_rain_effect += 1
  # rain_effect = random.randint(min_rain_effect, max_rain_effect)
  
  # if 'vacation' in day['events']:
  #   number_of_sales += random.randint(round(number_of_sales * 0.2), round(number_of_sales * 0.3))
    
  # return number_of_sales + rain_effect + temerature_effect + day_of_week_effect

# def create_random_hour():
#   random_hour = random.randint(0, 106)
#   if random_hour <= 35:
#     return (random_hour % 5) + 8
#   elif random_hour <= 60:
#     return (random_hour % 5) + 13
#   elif random_hour < 100:
#     return (random_hour % 5) + 18
#   else:
#     return 23
  
# def create_random_number_of_category(random_hour, day):
#   category1 = 100
#   category2 = 70
#   category3 = 60
#   category4 = 80
#   day_of_week = day['day_of_week']
#   temperature = None
#   try:
#     temperature = abs(round((day['max_temperature'] * 2) + day['min_temperature'] / 3))
#   except Exception as e:
#     temperature = 30
  
#   if random_hour <= 12:
#     category1 *= 2
#     category4 *= 0.9
#   if random_hour >= 11 and random_hour <= 17:
#     category2 *= 2
#   if random_hour < 18:
#     category4 *= 0.8
#   if random_hour >= 18:
#     category4 *= 2
    
#   if temperature < 25:
#     category2 *= 0.5
#     category1 *= 1.2
#   elif temperature < 35:
#     category4 *= 2
#     category3 *= 1.2
#   else:
#     category1 *= 0.4
#     category2 *= 1.5
#     category3 *= 1.2
#     category4 *= 0.5
    
#   if day_of_week == 1 or day_of_week == 4:
#     category4 *= 1.1
#   elif day_of_week < 5:
#     category4 *= 0.9
#   else:
#     category1 *= 0.8
#     category2 *= 0.7
#     category4 *= 1.5

#   random_number = random.randint(1, round(category1) + round(category2) + round(category3) + round(category4))
#   if random_number < category1:
#     return 0
#   elif random_number < category1 + category2:
#     return 1
#   elif random_number < category1 + category2 + category3:
#     return 2
#   else:
#     return 3
