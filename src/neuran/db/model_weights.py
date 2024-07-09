import pickle
from ..LSTM import model
from .index import get_model_weights_collection

def insert_model_data(user_name):
    model_weights_collection = get_model_weights_collection(user_name)
    
    model_data = model_weights_collection.find_one({'model_name': 'LSTM_model'})
    if model_data:
        weights_data = model_data['weights']
        model.set_weights(pickle.loads(weights_data))

def save_new_model_data(user_name):
    model_weights_collection = get_model_weights_collection(user_name)
  
    weights_data = pickle.dumps(model.get_weights())
    filter_query = {'model_name': 'LSTM_model'}
    update_query = {'$set': {'weights': weights_data}}
    model_weights_collection.update_one(filter_query, update_query, upsert=True)
