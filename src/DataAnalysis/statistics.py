from dataInitializer import day_of_year, temperatures, days_of_week, sales

# print(sum(sales) / len(sales))

def calculate_average(start_day_of_week, end_day_of_week, start_temperature, end_temperature):

    list_of_sales = []
    for day in day_of_year:
        day -= 1

        if days_of_week[day] in range(start_day_of_week, end_day_of_week + 1) and temperatures[day] in range(start_temperature, end_temperature + 1):
            list_of_sales.append(sales[day])

    if len(list_of_sales) == 0:
        return 0
    
    return round(sum(list_of_sales) / len(list_of_sales), 2)


def calculate_average_all_days_of_week(start_temperature, end_temperature):
    for day in range(1, 8):
        average = calculate_average(day, day, start_temperature, end_temperature)
        print(f'average for day {day}: {average}')

def calculate_average_all_temperatures(start_day_of_week, end_day_of_week):
    for temperature in range(8, 43):
        average = calculate_average(start_day_of_week, end_day_of_week, temperature, temperature)
        print(f'average for temperature {temperature}: {average}')

def smart_temperatures_average(start_day_of_week=1, end_day_of_week=7):
    for temperature in range(8, 43):
        average = calculate_average(start_day_of_week, end_day_of_week, temperature - 1, temperature + 1)
        print(f'average for temperature {temperature}: {average}')


# calculate_average_all_days_of_week(15, 35)
calculate_average_all_temperatures(1, 1)
# smart_temperatures_average(1, 1)


# def show_day_statistics(searching_day):
#     list_of_days = []

#     for day in day_of_year:
#         day -= 1
#         if X[1][day] == searching_day:
#             list_of_days.append({
#                 'temperatures': int(X[0][day]),
#                 'sales': Y[0][day]
#             })
    
#     list_of_days.sort(key=lambda x: x['temperatures'])

#     return list_of_days

# def show_temperature_statistics(searching_temperature):
#     list_of_days = []

#     for day in day_of_year:
#         day -= 1
        
#         if X[0][day] == searching_temperature:
#             list_of_days.append({
#                 'day_of_week': int(X[1][day]),
#                 'sales': Y[0][day]
#             })
    
#     list_of_days.sort(key=lambda x: x['day_of_week'])

#     return list_of_days


# # day_of_week_statistics = show_day_statistics(1)
# # [ print(day) for day in day_of_week_statistics ]
# temperatures_statistics = show_temperature_statistics(28)
# [ print(day) for day in temperatures_statistics ]