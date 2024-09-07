credits_taken = int(input('How many credits are you taking? '))
print('You are taking ' + str(credits_taken) + ' credits')

credits_taken_last_semester = int(input('How many credits did you take last semseter? '))
print('You took ' + str(credits_taken_last_semester) + ' credits last semester')

total_credits = credits_taken + credits_taken_last_semester
print('The total credits will be ' + str(total_credits) + ' in this and last semester')
