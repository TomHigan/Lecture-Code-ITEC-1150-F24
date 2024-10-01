# Two teams play a game. Ask the user for team 1's score.  Ask the user for team 2's score.
#
# Use conditional statements to print a message that says "Team 1 won" or "Team 2 won" or "It was a tie"
print('Who won the game?')
team_1 = int(input("What was Team 1's score?: "))
team_2 = int(input("What was Team 2's score?: "))

if team_1 > team_2:
    print('Team 1 won!')
elif team_1 < team_2:
    print('Team 2 won')
else:
    print('It was a tie!')