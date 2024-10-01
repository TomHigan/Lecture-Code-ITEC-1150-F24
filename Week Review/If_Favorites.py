# Write a program that asks for your favorite video game. Python's favorite video game is Tetris.
#
# Use an if statement to check if your favorite game is the same as Tetris. If it is, print the message 'Your favorite video game is the same as mine'
#
# Else, print the message 'We like different video games.'

#get user input to define favorite_videogame
favorite_videogame = input('What is your favorite video game?: ')
#use if/else statement to run print function in response to user input for favorite_videogame
if favorite_videogame.upper() == 'TETRIS':
    print('We have the same favorite video game!')
else:
    print('We like different video games!')

