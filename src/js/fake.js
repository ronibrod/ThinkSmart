console.log('Hi');

const FakeData = require('./dataFake.json');

const TYPES_OF_COFFEE = ['Espresso', 'Latte', 'Cappuccino'];
const RANGE_OF_TEMPERATURES = 1;

const statisticsByDay = () => {
    const daysData = [];

    TYPES_OF_COFFEE.map(typeOfCoffee => {
        daysData[typeOfCoffee] = [];

        for (let dayOfWeek = 1; dayOfWeek <= 7; dayOfWeek++) {
            const relevantDays = FakeData.filter(day => day.day_of_week === dayOfWeek);
            const sumOfSales = relevantDays.reduce((acc, current) => acc + current.sales[typeOfCoffee], 0);

            daysData[typeOfCoffee].push({
                day: dayOfWeek,
                sales: sumOfSales / relevantDays.length,
                weight: relevantDays.length,
            });
        }
    });

    return daysData;
};

const statisticsByTemperature = () => {
    const listOfTemperatures = FakeData.map(day => day.temperature_celsius);

    const minTemperature = Math.min(...listOfTemperatures);
    const maxTemperature = Math.max(...listOfTemperatures);

    const temperatureData = [];
    TYPES_OF_COFFEE.map(typeOfCoffee => {
        temperatureData[typeOfCoffee] = [];

        for (let temp = minTemperature; temp <= maxTemperature; temp += RANGE_OF_TEMPERATURES) {
            const listOfDays = FakeData.filter(day => day.temperature_celsius >= temp - RANGE_OF_TEMPERATURES && day.temperature_celsius <= temp + RANGE_OF_TEMPERATURES);
            const listOfSales = listOfDays.map(day => day.sales[typeOfCoffee]);
            const sumOfSales = listOfSales.reduce((acc, current) => acc + current, 0);

            temperatureData[typeOfCoffee].push({
                temperature: temp,
                sales: sumOfSales / listOfSales.length,
                weight: listOfSales.length,
            });
        }
    });

    return temperatureData;
};

const runStatistics = (searchDay, searchTemperature) => {
    const temperatureStatistics = statisticsByTemperature();
    const dayStatistics = statisticsByDay();

    TYPES_OF_COFFEE.map(typeOfCoffee => {
        const [temperatureData] = temperatureStatistics[typeOfCoffee].filter(temperatureInfo => temperatureInfo.temperature === searchTemperature);
        const [dayOfWeekData] = dayStatistics[typeOfCoffee].filter(dayOfWeekInfo => dayOfWeekInfo.day === searchDay);

        const expectedSale = ((temperatureData.sales * temperatureData.weight) + (dayOfWeekData.sales * dayOfWeekData.weight)) / (temperatureData.weight + dayOfWeekData.weight);

        console.log(`${typeOfCoffee}:`, expectedSale.toFixed(2));
    });
};

runStatistics(3, 28);
