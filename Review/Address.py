#variables with user input
house = input('What is your house number?: ')
street = input('What street do you live on?: ')
city = input('What city do you live in?: ')
state = input('What state do you live in?: ')
zip_code = input('What is your zip code?: ')

address = [house,street,city,state,zip_code] #list taking above variables and assigning them to the address
print(address)

users_address = '\n'.join(address) #lists the address sequentially on new lines
print('\nYour address is: \n'+users_address)

if address[2].lower() == "minneapolis": #checks if user is from minneapolis
    print("You live in Minneapolis!")
else:
    print("You do not live in Minneapolis.")
