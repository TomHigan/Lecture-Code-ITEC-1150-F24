quiz_score = float(input('Enter score for quiz out of 100:'))

if quiz_score == 100:
    print('Congrats! You got an A')
elif quiz_score >= 80:
    print('You got a B')
elif quiz_score >= 70:
    print('You got a C')
elif quiz_score >= 60:
    print('You got a D')
else:
    print('You failed the Class')