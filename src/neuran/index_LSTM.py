import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.metrics import MeanSquaredError
from sklearn.metrics import mean_squared_error, r2_score
from .LSTM import model
from .LSTM_operations import train_model, predict_model
from .input_data_for_training import get_days_data, create_input_data_for_training
from .output_data_for_training import get_output_data
from .const import user_name, user_name9

def run(user_name):
  
	# input_data = create_input_data_for_training(user_name)
	# output_data = get_output_data(user_name)

	X, Y, Y_scaler = get_days_data(user_name)

	# print(X.shape)
	# print(Y.shape)

	split_index = int(0.8 * len(X))
	X_train = X[:split_index]
	X_test = X[split_index:]
	Y_train = Y[:split_index]
	# Y_train = Y[:split_index]
	Y_test = Y[split_index:]


	# X_train = np.array(X_train.reshape(X_train.shape[0], 1, X_train.shape[1]))
	# X_test = np.array(X_test.reshape(X_test.shape[0], 1, X_test.shape[1]))
 
	# X_train = np.array([[0.1, 0.2], [0.2, 0.3], [0.3, 0.4], [0.4, 0.5], [0.5, 0.6]])
	# Y_train = np.array([0.3, 0.5, 0.7, 0.9, 1.1])
	# X_train = X[:320]
	# Y_train = Y[:320]
	
	# train_model(user_name, X_training, Y_training)
	model.fit(X_train, Y_train, epochs=20, batch_size=32)
 
	# layer_name = 'dense_1'  # You can find the layer name using model.summary() if needed
	# intermediate_layer_model = Model(inputs=model.input, outputs=model.get_layer(layer_name).output)

	# # Predict with the intermediate model to get the activations
	# intermediate_output = intermediate_layer_model.predict(X_test)

	# # Print the activations
	# print("Activations of the second Dense layer:")
	# print(intermediate_output)


	train_predictions = model.predict(X_train)
	# test_predictions = model.predict(X_test)
	# train_predictions = predict_model(user_name, X_training)
	# test_predictions = predict_model(user_name, X_testing)

	tf_mse = MeanSquaredError()

	print('\n---------------- train -----------------')

	train_tf_mse = tf_mse(Y_train, train_predictions)
	train_skl_mse = mean_squared_error(Y_train, train_predictions)
	train_sse = sum([(y - y_predic)**2 for y, y_predic in zip(Y_train, train_predictions)])
	train_r2 = r2_score(Y_train, train_predictions)
	
	print('tf_mse: ', train_tf_mse)
	print("skl_mse:", train_skl_mse)
	print("SSE div:", train_sse / len(Y_train))
	print("SSE all:", train_sse)
	print("R^2 Score:", train_r2)
	print('E', Y_scaler.inverse_transform(Y_train)[0], 'P', Y_scaler.inverse_transform(train_predictions)[0])
	print('E', Y_scaler.inverse_transform(Y_train)[-1], 'P', Y_scaler.inverse_transform(train_predictions)[-1])






	# test_mse = tf_mse(Y_test, test_predictions)
	# print(f"tf_mse: {test_mse}")
	# print(Y_train[:5])
	# print(X_train[:5])
	# print(train_predictions[:5])
	# print(Y_train[:5])
	# print(Y_test[:5])
	# print('train P', Y_scaler.inverse_transform(train_predictions[:5]))
	# print('train E', Y_scaler.inverse_transform(Y_train[:5]))
	# print('test P', Y_scaler.inverse_transform(test_predictions[:5]))
	# print('test E',Y_scaler.inverse_transform(Y_test[:5]))

 
 


	
	
	
	

	
 
 

 
# def get_sse(Y_train, train_predictions):
#     sse = sum([(y - y_predic)**2 for y, y_predic in zip(Y_train, train_predictions)])
#     return sse

# def reset_weights(model):
# 	for layer in model.layers:
# 		if hasattr(layer, 'kernel_initializer') and hasattr(layer, 'bias_initializer'):
# 			layer.kernel.assign(layer.kernel_initializer(tf.shape(layer.kernel)))
# 			layer.bias.assign(layer.bias_initializer(tf.shape(layer.bias)))

# Example usage
# reset_weights(model)
run(user_name)
