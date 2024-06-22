import matplotlib.pyplot as plt
from dataInitializer import day_of_year, temperatures, days_of_week, sales

# Plotting the data for visualization
def show_in_graph():
    plt.figure(figsize=(14, 5))

    plt.subplot(1, 2, 1)
    plt.plot(day_of_year, temperatures, label='Temperature')
    plt.xlabel('Day of the Year')
    plt.ylabel('Temperature (°C)')
    plt.title('Daily Temperature')

    plt.subplot(1, 2, 2)
    plt.plot(day_of_year, sales, label='Ice Cream Sales', color='r')
    plt.xlabel('Day of the Year')
    plt.ylabel('Ice Cream Sales')
    plt.title('Ice Cream Sales vs. Day of the Year')

    plt.tight_layout()
    plt.show()

show_in_graph()
