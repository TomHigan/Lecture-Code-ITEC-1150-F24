import random
want_to_quit = ''

while not want_to_quit: #empty strings are false. If user provides input it will terminate program.
    dice_value = random.randint(1, 6)
    print(f'You rolled a {dice_value}')
    want_to_quit = input('Press enter to roll again. Press other keys to quit.: ')