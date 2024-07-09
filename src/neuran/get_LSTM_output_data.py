from .LSTM_operations import predict_model
from .input_data_for_training import get_input_data
from .output_data_for_training import get_output_scaler

def get_LSTM_output_data(user_name, product):
    input_data = get_input_data(user_name)
    output_scaler = get_output_scaler(user_name, product)

    output_data = predict_model(user_name, input_data)
    
    output_data = output_data.reshape(output_data.shape[0] * output_data.shape[1], output_data.shape[2])
    return output_scaler.inverse_transform(output_data)

# print(get_LSTM_output_data('lizCafeteria', 'Espresso'))