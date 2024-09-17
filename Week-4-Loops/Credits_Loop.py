number_of_credits = int(input('How many credits are you taking this semester?: '))

while number_of_credits < 0:
    print('Error - Enter a 0 or a positive number ')
    number_of_credits = int(input('How many credits are you taking this semester?: '))
if number_of_credits >= 12:
    print('You are a full time student')
elif number_of_credits >=6:
    print('You are a part-time student')
else:
    print('You are less than part-time')
