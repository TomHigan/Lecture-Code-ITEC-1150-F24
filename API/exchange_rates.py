import requests

url = 'https://1150-exchange-rates.azurewebsites.net/latest?base=USD&symbols=EUR' #assign url to variable

dollars = float(input('Enter number of dollars: ')) #get user input

response = requests.get(url).json() #requests data from url
print(response) #prints the requested data

rates = response['rates'] #assigns the rates key to the rates variable
print(rates)

exchange_rate = rates['EUR']  #pulls the exchange rate of the EUR key within the rates dictionary and assigns it to the variable.
print(exchange_rate)

euros = dollars * exchange_rate #creates a equation to determine the value of euros in dollars
print(f'${dollars} is equal to {euros:.2f} euros.') #prints results