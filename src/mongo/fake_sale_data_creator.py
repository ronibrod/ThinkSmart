import random
from fake_day_data_creator import create_days_array
from fake_product_data_creator import create_products_array

def create_sales_array(start_date, end_date):
  salse_array = []
  list_of_days = create_days_array(start_date, end_date)
  list_of_products = create_products_array()

  for day in list_of_days:
    random_number_of_sales = random.randint(100, 250)

    for sale in range(random_number_of_sales):
      random_number_of_product = random.randint(0, len(list_of_products) - 1)
      salse_array.append({
        'sale_id': day['date'].strftime('%d/%m/%Y/%H/%M/%S') + '_' + list_of_products[random_number_of_product]['name'],
        'product': list_of_products[random_number_of_product]['name'],
        'category': list_of_products[random_number_of_product]['category'],
        'date': day['date'],
      })

  return salse_array
