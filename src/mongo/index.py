from datetime import datetime
from .pymongoServer import startCollection
from .fake_day_data_creator import create_days_array
from .fake_product_data_creator import create_products_array
from .fake_sale_data_creator import create_sales_array

collectionName = 'lizCafeteria'
# start_date = datetime(2022, 1, 1)
# end_date = datetime(2024, 7, 31)
start_date = datetime(2020, 1, 1)
end_date = datetime(2024, 5, 31)

collection = startCollection(collectionName)
dayCollection = collection['day']
productCollection = collection['product']
saleCollection = collection['sale']

# list_of_fake_days = create_days_array(start_date, end_date)
# list_of_fake_products = create_products_array()

# dayCollection.insert_many(list_of_fake_days)
# productCollection.insert_many(list_of_fake_products)

days = list(dayCollection.find({}))
products = list(productCollection.find({}))
list_of_fake_sales = create_sales_array(days, products)
saleCollection.insert_many(list_of_fake_sales)

print(len(list_of_fake_sales))
print(list_of_fake_sales[0])
print(list_of_fake_sales[-1])
