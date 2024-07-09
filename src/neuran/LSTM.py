import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Input

time_steps = 7
input_features = 7
output_features = 24

# Initialize the Sequential model
model = Sequential()

# model.add(Input(shape=(time_steps, input_features)))  # input layer for 7 days, 7 features
model.add(LSTM(units=7, input_shape=(time_steps, input_features), return_sequences=True))  # input layer for 7 days, 7 features
model.add(LSTM(200, return_sequences=True))  # First LSTM layer
model.add(LSTM(100, return_sequences=True))  # Second LSTM layer
model.add(Dense(128, activation='relu'))  # First Dense layer
model.add(Dense(64, activation='relu'))   # Second Dense layer
model.add(Dense(24))  # Output layer for 24 hours of sales predictions

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Display the model summary
# model.summary()
