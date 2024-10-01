#print something to give context of what this program is for.
print("What type of house plant should you get?")
#create variables temperature and light using user input
#use while loop to continuously ask for input if user types incorrectly.
while True:
    temperature = input('Is your home warm or cool?: ')
    if temperature.upper() == 'WARM' or temperature == 'COOL':
        break
    else:
        print('Please enter "warm" or "cool" only.')
while True:
    light = input('Does your home have sun or shade inside?: ')
    if light.upper() == 'SUN' or light == 'SHADE':
        break
    else:
        print('Please enter "sun" or "shade" only.')
#create if/else and statements to determine the proper plant to display in print function.
if temperature.upper() == 'COOL' and light.upper() == 'SHADE':
    print('You should get an ivy plant for your home!')
elif temperature.upper() == 'COOL' and light.upper() == 'SUN':
    print('You should get an jade plant for your home!')
elif temperature.upper() == 'WARM' and light.upper() == 'SHADE':
    print('You should get an begonia plant for your home!')
elif temperature.upper() == 'WARM' and light.upper() == 'SUN':
    print('You should get an hibiscus plant for your home!')