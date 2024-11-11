address_fields = ['house number','stree name', 'city','state','zip code']

address = {}

#
for field in address_fields:
    user_input = input(f'Enter your {field}: ')
    address[field] = user_input

print('Your address is:\n')
for key, value in address.items():
    print(f'{key}: {value}')
