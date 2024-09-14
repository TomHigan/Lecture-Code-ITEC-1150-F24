weight = float(input('Enter your weight in pounds: '))
age = int(input('Enter your age in years: '))

if weight >= 110 and age >= 16:
    print("You can donate blood")
else:
    print('Sorry you cannot donate blood')
    if age < 16:
        print('You are not old enough')
    if weight < 110:
        print('You do not weigh enough')
