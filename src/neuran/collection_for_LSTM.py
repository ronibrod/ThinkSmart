from pymongo import MongoClient

# MongoDB configuration
def get_model_weights_collection():
  client = MongoClient('localhost', 27017)
  db = client['lizCafeteria']
  model_weights_collection = db['model_weights']
  
  return model_weights_collection
