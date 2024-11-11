import random

favorite_movies = ['iron man', 'inside out', 'idiocracy'] #list of favorite moveies

for movies in favorite_movies: #prints movies sequentially
    print(movies)

favorite_movies.append('Spiderman') #adds spiderman to list
print(favorite_movies)

number_of_movies = len(favorite_movies) #determins the number of movies
print(number_of_movies)

random.shuffle(favorite_movies) #shuffles the order of the list
print(favorite_movies)

first_movie = favorite_movies[0] #assigns the first movie in the list to this variable
print(first_movie)

if ('Star Wars') in favorite_movies: #checks if a movie is in the list then prints the below messages
    print('The movie is in the list')
else:
    print('The movie is not in the list')