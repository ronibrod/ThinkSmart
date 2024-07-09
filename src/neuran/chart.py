import matplotlib.pyplot as plt
from .get_LSTM_output_data import get_LSTM_output_data
# from .db.days import get_list_of_days
# from dataInitializer import day_of_year, temperatures, days_of_week, sales

user_name = 'lizCafeteria'
product = 'Espresso'

sales_by_hour = get_LSTM_output_data(user_name, product)

sales = []
for sale in sales_by_hour:
    sales.append(sum(sale))
# list_of_days = get_list_of_days(user_name)
times = range(1, len(sales) + 1)

print(len(sales))
print(len(times))

def show_in_chart():
    plt.figure(figsize=(14, 5))

    # plt.subplot(1, 2, 1)
    plt.plot(times, sales, label='LSTM')
    plt.xlabel('Day')
    plt.ylabel('Sales')
    plt.title('Daily Sale')

    # plt.subplot(1, 2, 2)
    # plt.plot(times, sales, label='Ice Cream Sales', color='r')
    # plt.xlabel('Day of the Year')
    # plt.ylabel('Ice Cream Sales')
    # plt.title('Ice Cream Sales vs. Day of the Year')

    plt.tight_layout()
    plt.show()

show_in_chart()
