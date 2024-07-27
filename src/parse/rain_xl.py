import pandas as pd
from datetime import datetime, timedelta

first_date = '01/01/2020'
last_date = '31/05/2024'

def get_rain_data():
    file_path = r'C:\Users\ronib\Desktop\projects\Coffee\src\dataFiles\data_20240716853.xlsx'

    df = pd.read_excel(file_path)
    nested_array = df.values.tolist()

    filtered_array = [row[1:] for row in nested_array]
    formatted_data = [{'date': datetime.strptime(item[0], '%d/%m/%Y'), 'rain': item[1]} for item in filtered_array]
    
    full_rain_dates = []
    current_date = datetime.strptime(first_date, '%d/%m/%Y')
    end_date = datetime.strptime(last_date, '%d/%m/%Y')
    for item in formatted_data:
        while current_date < item['date'] and current_date < end_date:
            full_rain_dates.append({'date': current_date, 'rain': 0})
            current_date += timedelta(days=1)
        
        full_rain_dates.append(item)
        current_date += timedelta(days=1)
    
    while current_date <= end_date:
        full_rain_dates.append({'date': current_date, 'rain': 0})
        current_date += timedelta(days=1)
        
    return full_rain_dates

# print(len(get_rain_data()))
# print(get_rain_data()[-1])
