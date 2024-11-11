#1. Lists are used to store date in a specific order and
# dictionaries are used to correlate data with key and value pairs.
# Yes you can have multiple lists and dictionaries in one program.
# Yes you can utilize both of them together in one program
from pprint import pprint

topping_choices = ['pepperoni', 'mushrooms', 'peppers', 'onions', 'olives'] #list with the topping choices
topping_prices = {
    'pepperoni': 1.40,
    'mushrooms': 0.80,
    'peppers': 0.80,
    'onions': 1.00,
    'olives': 1.00
} #dictionary with topping prices

toppings_ordered = [] #empty dictionary to be filled with the user input

for toppings in topping_choices:
    topping_price = topping_prices[toppings]
    topping_price_half = topping_price / 2
    customers_order = input(f'Do you want {toppings} on the whole pizza,  left, or right ? \n' 
                            f'The price is ${topping_price:.2f} for the whole pizza, ${topping_price_half:.2f} for half the pizza \n'
                            f'Enter "W" for whole pizza, "L" for left only. "R" for right only, "N" for no topping:') #user input to determine where/if they want the topping
    if customers_order == 'W':
        topping_data = { 'name': toppings, 'position': 'whole pizza'}
        toppings_ordered.append(topping_data)
    elif customers_order == 'L':
        topping_data = {'name': toppings, 'position': 'left'}
        toppings_ordered.append(topping_data)
    elif customers_order == 'R':
        topping_data = {'name': toppings, 'position': 'right'}
        toppings_ordered.append(topping_data) #if statements to display where the user wants the toppings and then add it to the pizza order.
pprint(toppings_ordered)

base_price = 9.99
total_price = base_price

if len(toppings_ordered) == 0: #if the user selects no on all toppings it will display the below messages
    print('You have ordered a pizza with no toppings')
    print(f'The total price is ${base_price}')
else:
    print('You have ordered a pizza with these topping(s): ')

    for order in toppings_ordered:
        name = order['name']
        position = order['position']
        price_whole_pizza = topping_prices[name]
        price_half_pizza = price_whole_pizza / 2
        if position == 'whole pizza':
            print(f'{name} on {position}, cost ${price_whole_pizza:.2f}')
            total_price = total_price + price_whole_pizza
        else:
            print(f'{name} on {position}, cost ${price_half_pizza:.2f}')
            total_price = total_price + price_half_pizza
    print(f'The total is ${total_price:.2f}')





