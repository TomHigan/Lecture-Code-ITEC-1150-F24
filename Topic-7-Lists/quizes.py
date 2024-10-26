""" Changing a List Item"""

quiz_scores = [8,4,10,9,7]
print(quiz_scores)
#what if the user re-took the second quiz
#lets say the user aced the quiz and scored 10
#update the quiz_scores list

# quiz_scores[1] = 10
# print(quiz_scores)
quiz = int(input('Which quiz did you retake?: '))
score = int(input('What was your score on quiz 2?: '))

#subtract 1 from quiz to count as a human does rather than from 0
quiz_scores[quiz-1] = score
print(quiz_scores)