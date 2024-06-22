import json
import numpy as np

def json_to_array(json_file):
    # Load JSON data from file
    with open(json_file, 'r') as jsonfile:
        data = json.load(jsonfile)

    # Extract 'date' and 'value' fields from each item
    result = []
    for item in data:
        result.append({
            'date': item['date'],
            'value': item['value']
        })

    return result

def separate_data(data):
    dates = []
    values = []

    for item in data:
        day, month, year = item['date'].split('/')
        dates.append([int(day), int(month), int(year)])
        values.append(float(item['value']))

    dates_array = np.array(dates)
    values_array = np.array(values)

    dates_transposed = dates_array.T

    return dates_transposed, values_array

result_array = json_to_array('C:/Users/ronib/Desktop/projects/Coffee/src/parse/ChartData.json')
dates, values = separate_data(result_array)

# print("date =", dates)
# print("value =", values)
# print(result_array)
