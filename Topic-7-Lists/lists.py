#list of int values
lab_numbers = [1,2,3,4,5,6,7,8,9,10]

#list of float values
temps = [78,87.5,67.7,56.3]
first_day_temp = temps[0] #ties the first_day_temp variable to element 0 in temps list
print(f'The first day of the week was {first_day_temp}F')
temps[3] = 66.3 #changes element 3 in temps list to 66.3

#list of different things
example = [False, 4, 1234.567, 'Hello']

#lists of lists
lists = [example, temps, lab_numbers, [1,2,3]]
print(lists)