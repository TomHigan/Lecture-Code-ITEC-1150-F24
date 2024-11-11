house = input('What is your house number?: ')
street = input('What street do you live on?: ')
city = input('What city do you live in?: ')
state = input('What state do you live in?: ')
zip_code = input('What is your zip code?: ')

#creates a dictionary assigning above variables to keys in a dictionary
address = {'House Number': house,
           'Street Name': street,
           'City': city,
           'State': state,
           'Zip Code': zip_code}

for address_keys, address_values in address.items(): #prints the keys and values
    print(address_keys, address_values)

if address['City'].lower() == "minneapolis":
    print("You live in Minneapolis!")
else:
    print("You do not live in Minneapolis.")
