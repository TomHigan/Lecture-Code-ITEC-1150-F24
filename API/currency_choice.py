import requests

url = 'https://1150-exchange-rates.azurewebsites.net/latest?base=USD' #assigns url to url variable

response = requests.get(url).json() #gets data from url and assigns it to response variable
# print(response)
rates = response['rates'] #defines rates as dictionary with the data from response/api url
# print(rates)
print('USD conversion Calculator \n') #user friendly title

dollars = float(input('Enter the number of dollars:')) #user input to determine USD to convert

print(', '.join(rates.keys()),'\n') #pules the keys from the rates dictionary so the user knows the options available

print('Here are the available currency codes')
currency_code = input('Enter currency code to convert to: ') #user selects currency code

exchange_rate = rates.get(currency_code) #pulls the users entered currency code from the rates dictionary. Will return none rather than crash if invalid code is entered thanks to .get()
if exchange_rate: #if the exchange rate entered is valid run the below code
    converted_value = dollars * exchange_rate #mulitplies user inputs
    print(f'${dollars} is equal to {converted_value:.2F}{currency_code}') #displays conversion
else: #if user enters invalid currency code run below code.
    print('Not a valid currency code.')