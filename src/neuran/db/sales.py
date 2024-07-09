from .index import get_sales_collection

def get_first_and_last_sale_dates(user_name):
    sales_collection = get_sales_collection(user_name)
    first_sale = sales_collection.find_one({}, sort=[('date', 1)])  # Ascending order for the first sale
    last_sale = sales_collection.find_one({}, sort=[('date', -1)])  # Descending order for the last sale
    
    if first_sale and last_sale:
        return first_sale['date'], last_sale['date']
    else:
        return None, None

def get_list_of_sales(user_name, product):
    sales_collection = get_sales_collection(user_name)
    first_date, last_date = get_first_and_last_sale_dates(user_name)
    
    if not first_date or not last_date:
        return []
    
    query = {
      'date': {'$gte': first_date, '$lte': last_date},
      'product': product,
    }
    return list(sales_collection.find(query))
