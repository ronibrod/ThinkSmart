import pandas as pd

def get_temperature_data():
    file_path = r'C:\Users\ronib\Desktop\projects\Coffee\src\dataFiles\data_20240716855.xlsx'

    df = pd.read_excel(file_path)
    nested_array = df.values.tolist()

    filtered_array = [row[1:] for row in nested_array]
    formatted_data = [{'date': item[0], 'max': item[1], 'min': item[2]} for item in filtered_array]
    # formatted_data = pd.DataFrame(formatted_data)
    # formatted_data.fillna(method = 'bfill', inplace=True)
    # formatted_data.fillna(formatted_data.mean(), inplace=True)
    # formatted_data = formatted_data.max.fillna(formatted_data.max.median())
    
    return formatted_data

# print(len(get_temperature_data()))
# print(get_temperature_data()[-1])
