import numpy as np
from .LSTM import model
from .input_data_for_training import get_input_data
from .output_data_for_training import get_output_data
from .db.model_weights import insert_model_data, save_new_model_data
from .const import product

def predict_model(user_name, input_data):
    insert_model_data(user_name)
    return model.predict(input_data)

def train_model(user_name):
    input_data = get_input_data(user_name)
    output_data = get_output_data(user_name, product)
      
    insert_model_data(user_name)
  
    model.fit(input_data, output_data, epochs=10000, batch_size=32)
  
    save_new_model_data(user_name)
