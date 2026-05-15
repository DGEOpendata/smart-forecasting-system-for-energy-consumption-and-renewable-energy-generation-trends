python
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Load electricity consumption data
electricity_data = pd.read_csv('Electricity_Consumption_by_Sector.csv')
renewable_data = pd.read_csv('Renewable_Energy_Generation.csv')

# Preprocessing: Parse dates and set index
electricity_data['Year'] = pd.to_datetime(electricity_data['Year'], format='%Y')
electricity_data.set_index('Year', inplace=True)
renewable_data['Year'] = pd.to_datetime(renewable_data['Year'], format='%Y')
renewable_data.set_index('Year', inplace=True)

# Aggregate electricity consumption data for all sectors
electricity_data['Total_Consumption'] = electricity_data.sum(axis=1)

# Build ARIMA model for electricity consumption
model = ARIMA(electricity_data['Total_Consumption'], order=(5,1,0))
model_fit = model.fit()

# Forecast next 5 years
forecast = model_fit.forecast(steps=5)
print("Electricity Consumption Forecast for Next 5 Years:")
print(forecast)

# Plot the forecast
plt.plot(electricity_data.index, electricity_data['Total_Consumption'], label='Historical Data')
plt.plot(pd.date_range(electricity_data.index[-1], periods=6, freq='Y')[1:], forecast, label='Forecast', color='red')
plt.legend()
plt.title('Electricity Consumption Forecast')
plt.xlabel('Year')
plt.ylabel('Electricity Consumption (GWh)')
plt.show()

# Repeat similar steps for renewable energy generation data
# Add more advanced forecasting models like LSTM for better predictions
