import numpy as np
from .LSTM import model  # Assuming you import your LSTM model
from .data_for_training_LSTM import get_training_data
from .LSTM_operations import predict_model

num_days_per_week = 7  # Days per week
num_hours_per_day = 24  # Hours per day

def export_predicted_output(predicted_output, output_data, output_scaler):
    # Reshape predicted_output and output_data to 2D for inverse transform
    num_samples = predicted_output.shape[0]
    predicted_output_reshaped = predicted_output.reshape(num_samples * num_days_per_week, num_hours_per_day)
    output_data_reshaped = output_data.reshape(num_samples * num_days_per_week, num_hours_per_day)
    
    # Inverse transform the reshaped data to original scale
    predicted_output_original_scale = output_scaler.inverse_transform(predicted_output_reshaped)
    output_data_original_scale = output_scaler.inverse_transform(output_data_reshaped)

    # Reshape back to the original 3D shape
    predicted_output_original_scale = predicted_output_original_scale.reshape(num_samples, num_days_per_week, num_hours_per_day)
    output_data_original_scale = output_data_original_scale.reshape(num_samples, num_days_per_week, num_hours_per_day)

    # You can now compare the reshaped predicted output with the actual output
    # For example, print a sample
    # print("Sample predicted output:", predicted_output_original_scale[0])
    # print("Sample actual output:", output_data_original_scale[0])
    
    predicted_sum_first_week = np.sum(predicted_output_original_scale[:10])
    actual_sum_first_week = np.sum(output_data_original_scale[:10])

    print("Sample predicted output sum for first week:", predicted_sum_first_week)
    print("Sample actual output sum for first week:", actual_sum_first_week)

# Load the training data and scaler
input_data, output_data, output_scaler = get_training_data()
input_data = input_data.astype(np.float32)
output_data = output_data.astype(np.float32)

# Ensure input_data is reshaped to match the expected shape (num_samples, num_days_per_week, num_features)
# No need to reshape input_data here as it's already in the correct shape for the LSTM model

# Example predicted output (replace with actual model prediction)
predicted_output = predict_model(input_data)

# Call the function with the necessary arguments
export_predicted_output(predicted_output, output_data, output_scaler)
