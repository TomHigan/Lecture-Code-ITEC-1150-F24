# Invoice Program
# • Ask for the name of a product sold
product = input('What is the product name? ')

# • Ask how many were sold
items_sold = int(input('How many items were sold? '))

# • Ask for the price of one item
item_price = float(input('How much does on item cost? '))

# • Do the math to figure out the total price
total = items_sold * item_price

# • Print a neat invoice with all the data in
# • Comment code
print()
print(product + ' Sales')
print('Quantity Sold: ' + str(items_sold))
print('Item price: ' + str(item_price))
print('Total: $' + str(total))