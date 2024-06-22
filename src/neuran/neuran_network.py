import numpy as np

# Activation function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Initialize parameters
def initialize_parameters(input_size, hidden_size, output_size):
    np.random.seed(1)
    W1 = np.random.randn(hidden_size, input_size) * 0.01
    b1 = np.zeros((hidden_size, 1))
    W2 = np.random.randn(output_size, hidden_size) * 0.01
    b2 = np.zeros((output_size, 1))
    
    parameters = {
        "W1": W1,
        "b1": b1,
        "W2": W2,
        "b2": b2
    }
    
    return parameters

# Forward propagation
def forward_propagation(X, parameters):
    W1 = parameters['W1']
    b1 = parameters['b1']
    W2 = parameters['W2']
    b2 = parameters['b2']
    
    Z1 = np.dot(W1, X) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    
    cache = {
        "Z1": Z1,
        "A1": A1,
        "Z2": Z2,
        "A2": A2
    }
    
    return A2, cache

# Compute cost
def compute_cost(A2, Y):
    m = Y.shape[1]
    cost = (1 / (2 * m)) * np.sum((A2 - Y) ** 2)
    return cost

# Backward propagation
def backward_propagation(parameters, cache, X, Y):
    m = X.shape[1]
    
    W1 = parameters['W1']
    W2 = parameters['W2']
    
    A1 = cache['A1']
    A2 = cache['A2']
    
    dZ2 = A2 - Y
    dW2 = (1 / m) * np.dot(dZ2, A1.T)
    db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)
    
    dZ1 = np.dot(W2.T, dZ2) * A1 * (1 - A1)
    dW1 = (1 / m) * np.dot(dZ1, X.T)
    db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)
    
    grads = {
        "dW1": dW1,
        "db1": db1,
        "dW2": dW2,
        "db2": db2
    }
    
    return grads

# Update parameters
def update_parameters(parameters, grads, learning_rate):
    W1 = parameters['W1'] - learning_rate * grads['dW1']
    b1 = parameters['b1'] - learning_rate * grads['db1']
    W2 = parameters['W2'] - learning_rate * grads['dW2']
    b2 = parameters['b2'] - learning_rate * grads['db2']
    
    parameters = {
        "W1": W1,
        "b1": b1,
        "W2": W2,
        "b2": b2
    }
    
    return parameters

# Training the model
def model(X, Y, hidden_size, num_iterations, learning_rate):
    np.random.seed(1)
    input_size = X.shape[0]
    output_size = Y.shape[0]
    
    parameters = initialize_parameters(input_size, hidden_size, output_size)
    
    for i in range(num_iterations):
        A2, cache = forward_propagation(X, parameters)
        cost = compute_cost(A2, Y)
        grads = backward_propagation(parameters, cache, X, Y)
        parameters = update_parameters(parameters, grads, learning_rate)
        
        if i % 20000 == 0:
            print(f"Cost after iteration {i}: {cost}")
    
    return parameters

# Predict function
def predict(X, parameters):
    A2, _ = forward_propagation(X, parameters)
    return A2



# # Example data (temperatures and days, and corresponding ice cream sales)
# X = np.array([[30, 32, 34, 36, 38, 40],  # Temperatures
#               [1, 2, 3, 4, 5, 6]])       # Days of the week

# Y = np.array([[200, 220, 240, 260, 280, 300]])  # Ice cream sales
# max_Y = np.max(Y)

# # Normalize data (optional, but recommended for better performance)
# X = X / np.max(X, axis=1, keepdims=True)
# Y = Y / np.max(Y)

# # Train the neural network
# hidden_size = 4
# num_iterations = 1000000
# learning_rate = 0.01

# parameters = model(X, Y, hidden_size, num_iterations, learning_rate)

# # Make predictions
# test_X = np.array([[31, 38, 34, 36, 32, 39],  # Temperatures
#                   [1, 2, 3, 4, 5, 6]])       # Days of the week
# test_X = test_X / np.max(test_X, axis=1, keepdims=True)

# original_predictions = predict(test_X, parameters) * max_Y
# formatted_predictions = ["{:.1f}".format(num) for num in original_predictions.flatten()]

# print("Formatted Predictions:", formatted_predictions)
