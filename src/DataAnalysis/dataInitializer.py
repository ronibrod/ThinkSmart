import numpy as np

np.random.seed(0)  # For reproducibility

# Constants
days_in_year = 365
base_temp = 25  # Average baseline temperature
temp_amplitude = 10  # Temperature variation amplitude
noise_strength = 4  # Temperature random daily fluctuation

# Generating day of the year
day_of_year = np.arange(1, days_in_year + 1)

# Temperature model: sinusoidal change through the year + random noise
temperatures = (base_temp + temp_amplitude * np.sin(2 * np.pi * day_of_year / 365) +
                np.random.normal(0, noise_strength, days_in_year))
temperatures = np.round(temperatures).astype(int)

# Day of the week (1=Monday, 7=Sunday)
days_of_week = np.tile(np.arange(1, 8), days_in_year // 7 + 1)[:days_in_year]
days_of_week = np.round(days_of_week).astype(int)

# Ice cream sales model
# Assume sales are directly proportional to temperature and slightly higher on weekends
base_sales = 100  # Base sales at lowest temperature
sales = (base_sales + (temperatures - base_temp) * 10 + 
        40 * np.sin(2 * np.pi * (8 - days_of_week) / 7))

# Normalize the sales to make sure minimum sales are always positive
sales -= np.min(sales) - 50
sales = np.round(sales).astype(int)
