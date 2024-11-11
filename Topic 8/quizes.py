#each student took 3 quizzes
quiz_scores = {
    'Al': [8,9,15],
    'Bettina': [6,10,10],
    'Cody': [7,7,9]
}

#loop with data from quiz_scores
for student, scores in quiz_scores.items():
    print(f' Student {student} scores are {scores}')

#retreive one students quiz scores
cody_scores = quiz_scores['Cody']

#print out codys scores sequentially
for i, score in enumerate(cody_scores): #i represents each value or quiz
    print(f'On quiz {i+1} Cody scored {score}') #need to add 1 to i because python starts counting at 0

cody_max = max(cody_scores)
print(f'Cody\'s best score is {cody_max}')

#retrieve bettina's lowest score
bettina_min = min(quiz_scores['Bettina']) #instead of a new variable i nested the score retrieval code within the min function.
print(f'Bettina\'s lowest score was {bettina_min}')
