from .LSTM_operations import train_model
from .const import user_name

def run(user_name):
	train_model(user_name)

run(user_name)
