import requests
import datetime

api_key = "YOUR_API_KEY"
lat = 32.0853
lon = 34.7818

today = datetime.datetime.now()
timestamps = [(today - datetime.timedelta(days=i)).timestamp() for i in range(1, 366)]

def fetch_temperature(api_key, lat, lon, timestamp):
    url = f"http://api.openweathermap.org/data/2.5/onecall/timemachine"
    params = {
        'lat': lat,
        'lon': lon,
        'dt': timestamp,
        'appid': api_key
    }
    response = requests.get(url, params=params)
    data = response.json()
    if 'current' in data:
        temperature_kelvin = data['current']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        return temperature_celsius
    else:
        return None

def temperatures_of_peroid(renge_of_time):
    temperatures = []
    for timestamp in timestamps:
        temperature = fetch_temperature(api_key, lat, lon, int(timestamp))
        print(api_key, lat, lon, int(timestamp))
        if temperature is not None:
            temperatures.append(temperature)
        else:
            temperatures.append('Data not available')

    return temperatures

list_of_temperatures = temperatures_of_peroid(timestamps)
print(list_of_temperatures)
