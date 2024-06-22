import numpy as np

from ..parse.json_to_array import dates, values
from ..DataAnalysis.dataInitializer import day_of_year, temperatures, days_of_week, sales
from .neuran_network import model, predict

# Train the neural network
hidden_size = 9
num_iterations = 100000
learning_rate = 0.2

# Normalize data for neural network
X = np.vstack((temperatures, days_of_week, day_of_year))
Y = sales.reshape(1, -1)

# X = dates
# Y = values.reshape(1, -1)

max_X = np.max(X, axis=1, keepdims=True)
max_Y = np.max(Y)
X = X / np.max(X, axis=1, keepdims=True)
Y = Y / np.max(Y)

parameters = model(X, Y, hidden_size, num_iterations, learning_rate)

# Make predictions
test_X = np.array([[28], [3], [180]])
test_X = test_X / np.max(max_X, axis=1, keepdims=True)

# print('parameters: ', parameters)

original_predictions = predict(test_X, parameters) * max_Y
formatted_predictions = ["{:.1f}".format(num) for num in original_predictions.flatten()]

print("Formatted Predictions:", formatted_predictions)
