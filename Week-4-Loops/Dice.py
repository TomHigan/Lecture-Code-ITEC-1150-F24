import random

number_of_dice = int(input('How many dice would you like to roll?: '))

# print('about to roll ' + str(number_of_dice) + ' dice')
print(f'Rolling {number_of_dice} dice.')

for dice in range(number_of_dice): #roll 5 dice
    dice_value = random.randint(1, 6)
    print(f'Dice {dice+1} value is {dice_value}')
