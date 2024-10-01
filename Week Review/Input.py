# Write a program that asks the user what color your shirt (or dress, or sweater...) is today.
#
# Python's favorite color is the same as your shirt.  Print a message that says  'Blue is my favorite color. You look nice today!'  The color should be the same color that you entered.


#ask user for input to define favorite color variable
favorite_color = input('What color is your shirt?: ')
#print sentence using favorite color variable. .capitalize will capitalize the first letter in the users input.
print(f'{favorite_color.capitalize()} is my favorite color. You look nice today!')