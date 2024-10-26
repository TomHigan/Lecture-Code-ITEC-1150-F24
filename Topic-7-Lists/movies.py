import random

favorite_movies = ['Idiocracy', 'Office Space', 'Marvel']

#sorts alphabetically
#reverses alphabetical order
#prints movies in sequence
favorite_movies.sort()
favorite_movies.reverse()
for movies in favorite_movies:
    print(movies)

#separates items in list by #
best_movies = ' # '.join(favorite_movies)
print(best_movies)

#adds spiderman and lion king to the end of the list
favorite_movies.append('SpiderMan')
favorite_movies.append('Lion King')
print(favorite_movies)

#randomly shuffles the order of the favorite_movies list
random.shuffle(favorite_movies)

#index is tied to the number that the element is in the list
#using +1 makes it count human like
#
for index, movies in enumerate(favorite_movies):
    print(f'{index+1}: {movies}')

#len is used to determine how many elements are in the favorite_movies list
number_of_movies = len(favorite_movies)
print(f'There are {number_of_movies} movies in the list')

# favorite_movies.remove('Marvel')
# print(favorite_movies)
# favorite_movies.remove('Marvel')
# print(favorite_movies)

#pop removes the element in that position on the list
movie_removed = favorite_movies.pop(0)
print(favorite_movies)
#this prints the element that was removed
print(movie_removed)
#leaving empty brackets removes the last element in the list
last_movie = favorite_movies.pop()
print(favorite_movies)
print(last_movie)