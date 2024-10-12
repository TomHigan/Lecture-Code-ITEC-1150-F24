import random

def main():
    #interacts with user for number of dice
    number_of_dice = int(input("How many dice to roll?: "))
    #calling the roll_dice function with an argument of the number_of_dice variable
    roll_dice(number_of_dice)
    #prints message at the end of the function
    print('That was all the dice')

#turns number_of_dice argument from above into a parameter to determine how many dice to roll
def roll_dice(number_of_dice):
    #rolling the dice with the user input from above
    for dice_count in range(number_of_dice):
        #indicates that the variable needs a random number from 1-6.
        dice_roll = random.randint(1,6)
        print(f'The dice rolled a {dice_roll}')

main()

