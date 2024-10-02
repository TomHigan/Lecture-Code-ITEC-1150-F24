# Write a program that asks the user for a 4-letter department code, for example ENGL or MATH or ITEC or SPAN or WEBI.
# Use a while loop to validate that the code is exactly 4 letters. If it is, print a 'thank you for the data' message.

#get input for department code
department_code = input('Type a 4 letter department code from your school: ')
#while len != will run the print/input again if the input doesnt equal the defined length of 4.
while len(department_code) != 4:
    print('Error - please enter a 4-letter department code')
    department_code = input('Type a 4 letter department code from your school.: ')
print(f'Thank you your department code is {department_code.upper()}.')