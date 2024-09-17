star_id = input('Enter your StarID: ')

while len(star_id) != 8:
    print('Error - please enter a valid StarID')
    star_id = input('Enter your StarID: ')
print(f'Thank you your StarID is {star_id}.')