movies_ratings = {'Harry Potter' : 7,
                  'Iron Man' : 8,
                  'Inside Out': 7,
                  'Idiocracy' : 6,
                  'Batman': 4}
print(movies_ratings)

#print a movie rating
harrypotter_rating = movies_ratings['Harry Potter']
print(harrypotter_rating)

#change a value
movies_ratings['Idiocracy'] = 3
print(movies_ratings)

#adding new data
movies_ratings['Dark Knight'] = 6
movies_ratings['Cloudy with a Chance of Meatballs'] = 8
print(movies_ratings)

#print keys of the dictionary
for movie in movies_ratings:
    print(movie)

#print the keys and the values
for movie, rating in movies_ratings.items():
    print(movie, rating)

#get a value for a key that exists/doesnt exist
batman_rating = movies_ratings.get('Batman')
print(batman_rating)

if batman_rating is None:
    print('There is no rating for Batman in the dictionary')
else:
    print(f'Batmans rating is {batman_rating} ')

dark_knight_rating = movies_ratings

#check if a key is in the dictionary
if 'Batman' in movies_ratings:
    print('Batman is one of the movies')
else:
    print('Batman is not one of the movies')

#remove a key
# print(movies_ratings)
# movies_ratings.pop('Batman')
# print(movies_ratings)

#remove a key but store the value
print(movies_ratings)
batman_rating = movies_ratings.pop('Batman')
print(batman_rating)
print(movies_ratings)