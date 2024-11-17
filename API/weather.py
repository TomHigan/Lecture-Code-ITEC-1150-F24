import requests

url = 'https://api.weather.gov/gridpoints/MPX/107,71/forecast' #url variable for the url of api

response = requests.get(url).json() #requests and assigns api data to variable
# print(response)

properties = response['properties'] #defines the properties dictionary with the properties key within the above api
# print(properties)
forecast_periods = properties['periods'] #assigns forecast_periods to a nested key within the properties dictionary
# print(forecast_periods)

for period in forecast_periods: #for loop to assign variables to values within the forecast_periods dictionary
    name = period['name']
    temp = period['temperature']
    forcast = period['detailedForecast']
    print(f'{name:<17}{temp:<17}{forcast}') #prints values with proper formating for readability