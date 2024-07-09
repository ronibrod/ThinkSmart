from pymongo import MongoClient

# user_name = 'lizCafeteria'

# MongoDB configuration
client = MongoClient('localhost', 27017)

def get_model_weights_collection(user_name):
  return client[user_name]['model_weights']

def get_sales_collection(user_name):
  return client[user_name]['sale']

def get_days_collection(user_name):
  return client[user_name]['day']
  