import math
import random
from fake_day_data_creator import create_days_array
from fake_product_data_creator import create_products_array

def create_sales_array(start_date, end_date):
  salse_array = []
  list_of_days = create_days_array(start_date, end_date)
  list_of_products = create_products_array()
  products_by_category = get_products_by_category(list_of_products)
  list_of_categories = list(products_by_category.keys())

  for day in list_of_days:
    number_of_sales = get_number_of_sales(day)

    for sale in range(number_of_sales):
      random_hour = create_random_hour()
      random_minute = random.randint(0, 59)
      time = day['date']
      time = time.replace(hour=random_hour, minute=random_minute)
      
      random_number_of_category = create_random_number_of_category(random_hour, day)
      random_number_of_product = random.randint(0, len(products_by_category[list_of_categories[random_number_of_category]]) - 1)
      
      salse_array.append({
        'sale_id': f'{sale}' + '_' + time.strftime('%d/%m/%Y_%H:%M:%S') + '_' + list_of_products[random_number_of_product]['name'],
        'product': products_by_category[list_of_categories[random_number_of_category]][random_number_of_product]['name'],
        'category': products_by_category[list_of_categories[random_number_of_category]][random_number_of_product]['category'],
        'date': time,
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

def get_number_of_sales(day):
  number_of_sales = random.randint(200, 250) # base
  
  day_of_week_effect = round(math.sin(math.pi * (((day['day_of_week'] + 6) % 8) / 8))) # add by day of week
  day_of_week_effect += random.randint(round(day_of_week_effect * 20), round(day_of_week_effect * 50))
  
  min_temerature_effect = round(6 - abs(day['temperature'] - 30))
  max_temerature_effect = round(random.randint(1, 20) + (min_temerature_effect * 2))
  if min_temerature_effect > max_temerature_effect:
    min_temerature_effect, max_temerature_effect = max_temerature_effect, min_temerature_effect
  elif min_temerature_effect == max_temerature_effect:
    max_temerature_effect += 1

  temerature_effect = random.randint(min_temerature_effect, max_temerature_effect)
  
  min_rain_effect = round((1 - day['rain']) - 1 ** 3)* 20
  max_rain_effect = min_rain_effect * 5
  if min_rain_effect > max_rain_effect:
    min_rain_effect, max_rain_effect = max_rain_effect, min_rain_effect
  elif min_rain_effect == max_rain_effect:
    max_rain_effect += 1
  rain_effect = random.randint(min_rain_effect, max_rain_effect)
  
  if 'vacation' in day['events']:
    number_of_sales += random.randint(round(number_of_sales * 0.2), round(number_of_sales * 0.3))
    
  return number_of_sales + rain_effect + temerature_effect + day_of_week_effect

def create_random_hour():
  random_hour = random.randint(0, 106)
  if random_hour <= 35:
    return (random_hour % 5) + 8
  elif random_hour <= 60:
    return (random_hour % 5) + 13
  elif random_hour < 100:
    return (random_hour % 5) + 18
  else:
    return 23
  
def create_random_number_of_category(random_hour, day):
  category1 = 100
  category2 = 70
  category3 = 60
  category4 = 80
  temperature = day['temperature']
  day_of_week = day['day_of_week']
  
  if random_hour <= 12:
    category1 *= 2
    category4 *= 0.9
  if random_hour >= 11 and random_hour <= 17:
    category2 *= 2
  if random_hour < 18:
    category4 *= 0.8
  if random_hour >= 18:
    category4 *= 2
    
  if temperature < 25:
    category2 *= 0.5
    category1 *= 1.2
  elif temperature < 35:
    category4 *= 2
    category3 *= 1.2
  else:
    category1 *= 0.4
    category2 *= 1.5
    category3 *= 1.2
    category4 *= 0.5
    
  if day_of_week == 1 or day_of_week == 4:
    category4 *= 1.1
  elif day_of_week < 5:
    category4 *= 0.9
  else:
    category1 *= 0.8
    category2 *= 0.7
    category4 *= 1.5

  random_number = random.randint(1, round(category1) + round(category2) + round(category3) + round(category4))
  if random_number < category1:
    return 0
  elif random_number < category1 + category2:
    return 1
  elif random_number < category1 + category2 + category3:
    return 2
  else:
    return 3
