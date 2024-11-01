#creat a list of the months
summer_months = ['June', 'July', 'August']

#create an empty dictionary to be filled with user input
rainfall ={}

#for loop using input to determine the amount of rainfall per month.
for month in summer_months:
    rain = float(input(f'How much rain was there in {month}, in inches?: '))
    rainfall[month] = rain #user input from above will then fill the key/value pair. Month and rain in that month.

print()

#print out data that is entered
print('Here is what you entered: ')
for month, rain in rainfall.items(): #takes the key/value pair from rainfall and assigns month to the keys and rain to the values
    print(f'In {month} there was {rain} inches of rain. ') #inputs the data from line above into string showcasing input.

print()

#use sum of values to determine total rainfall
total_rain = sum(rainfall.values())
print(f'The total amount of rainfall is {total_rain} inches')

print()

#average rainfall
months = len(rainfall) #determines how many pairs there are in the rainfall dictionary
average = total_rain/months #divides the total amount of rain by the number of months (3)
print(f'The average rainfall per month is {average} inches')
