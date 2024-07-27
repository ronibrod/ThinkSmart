import os
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Input, Reshape
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.initializers import HeNormal
from .const import time_steps

# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

time_steps = 1
input_features = 10
output_features = 1

# Initialize the Sequential model
model = Sequential()

model.add(Input(shape=(input_features,)))  # input layer for 7 days, features
# model.add(Dense(32, activation='relu', input_shape=(input_features,)))
# model.add(LSTM(units=50, input_shape=(time_steps, input_features), return_sequences=True))  # input layer for 7 days, features
# model.add(LSTM(200, return_sequences=True))  # First LSTM layer
# model.add(LSTM(100, return_sequences=False))  # Second LSTM layer
# model.add(Dense(128, activation='relu'))  # First Dense layer
model.add(Dense(64, activation='relu'))   # Second Dense layer
model.add(Dense(1, activation='linear'))  # Output layer for 24 hours of sales predictions

# with tf.variable_creator_scope('input'):
#   X = tf.placeholder(tf.int32, shape=(None, input_features))
# model.add(Input(shape=(input_features,)))
# model.add(Dense(128, activation='relu', kernel_initializer=HeNormal()))
# model.add(Reshape((1, 128)))  # Reshape to (batch_size, time_steps, features)

# # Add an LSTM layer for sequence data
# model.add(LSTM(64, activation='relu'))
# model.add(Dense(1, activation='linear', kernel_initializer=HeNormal()))

# optimizer = Adam(learning_rate=0.001)
# model.compile(optimizer=optimizer, loss='mean_squared_error')

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')
# model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Display the model summary
# model.summary()
