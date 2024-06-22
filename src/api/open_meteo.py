import openmeteo_requests
import requests_cache
from retry_requests import retry

# Setup the API client with caching and retry
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# API call setup
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "daily": ["temperature_2m_max", "temperature_2m_min"],
    "timezone": "Asia/Jerusalem",
    "start_date": "2023-01-01",
    "end_date": "2023-01-31"
}
responses = openmeteo.weather_api(url, params=params)

# Accessing attributes correctly by calling methods
latitude = responses[0].Latitude()
longitude = responses[0].Longitude()
timezone = responses[0].Timezone()

print("Latitude:", latitude)
print("Longitude:", longitude)
print("Timezone:", timezone)

# Assuming the daily weather data has a method to convert to a dictionary or similar structure
if hasattr(responses[0], 'Daily'):
    daily_data = responses[0].Daily()

# Assuming daily_data is already obtained and is a VariablesWithTime object
if not daily_data.VariablesIsNone() and daily_data.VariablesLength() > 0:
    for i in range(daily_data.VariablesLength()):
        variable = daily_data.Variables(i)
        print("Variable:", variable.Variable())  # Check what type of variable it is
        print("Unit of measure:", variable.Unit())  # Print the unit of measure
        
        # If this variable is temperature and values are available
        if not variable.ValuesIsNone():
            if variable.ValuesAsNumpy() is not None:  # Check if the numpy array is not empty
                values = variable.ValuesAsNumpy()
                print("Temperature values as numpy array:", values)
            else:
                values = [variable.Values(j) for j in range(variable.ValuesLength())]  # Loop through values if it's not in numpy format
                print("Temperature values:", values)
else:
    print("No variables available in this 'VariablesWithTime' object.")
