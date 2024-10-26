streets = ['Lake', 'Hennepin', 'Lyndale'] #creates list
print(streets) #prints the streets list

#prints the list item correlated to number in []
print(streets[0])
print(streets[1])
print(streets[2])

#changes item 0 in streets list to Chicago
streets[0] = 'Chicago'
print(streets)

#changes element 1 and 2 in streets list
streets[1] = 'Franklin'
print(streets)

streets[2] = 'Irving'
print(streets)

#print the streets in sequence
for street in streets:
    print(street)

#creates delivery_instructions variable
delivery_instructions = 'Please deliver to these streets '

#for loop that adds the delivery instructions string variable in front of the street list to print a sentence.
for street in streets:
    delivery_instructions = delivery_instructions + street + ','

print(delivery_instructions)