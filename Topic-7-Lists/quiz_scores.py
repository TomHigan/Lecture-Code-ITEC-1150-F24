#prints the number 0 five times, but in list format
quiz_scores = [0] * 5
print(quiz_scores)

#enumerate pairs the index in quiz_score with its corresponding score
#loop will run once for each item in quiz_score. currently set to 5
#each loop will assign a quiz_score to the current score related to the index (quiz)
for quiz, score in enumerate(quiz_scores):
    #asks user for input to assign scores to the new score variable. Using +1 to count human like
    new_score = int(input(f'Enter score for quiz {quiz+1}: '))
    #updates quiz_score with the new score value for the current quiz index
    quiz_scores[quiz] = new_score

print('You scores are ')
print(quiz_scores)