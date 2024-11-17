import requests

data = requests.get('https://catfact.ninja/fact').json() #assign api data to the data variable and turn it into a python dictionary
print(data) #will print the data variable as a python dictionary

fact = data['fact'] #assigns the value of fact from the data dictionary to the fact variable
print('\n') #provides space between printouts
print('A cat fact is: ' + fact) #prints string with only the value (fact) from the data dictionary