from datetime import timedelta
from .index import get_days_collection
from .sales import get_first_and_last_sale_dates

def get_list_of_days(user_name):
    days_collection = get_days_collection(user_name)
    first_date, last_date = get_first_and_last_sale_dates(user_name)
    
    if not first_date or not last_date:
        return []
      
    first_date = first_date - timedelta(days=1)
    last_date = last_date + timedelta(days=1)
    first_date = first_date.replace(hour=0, minute=0, second=0, microsecond=0)
    last_date = last_date.replace(hour=0, minute=0, second=0, microsecond=0)
    
    query = {'date': {'$gte': first_date, '$lte': last_date}}
    return list(days_collection.find(query))
