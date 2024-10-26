#make empty list
todo_list = []

while True:
    task =input('Enter your task, or press enter to stop: ')
    if task: #loop continues if user enters a string
        if task in todo_list:
            print('You already added that task')
        else:
            todo_list.append(task) #adds task to end of todo_list
    else:
        break #ends loops if user entered empty string
print('Thank you. Your tasks are: ')

for index, task in enumerate(todo_list): #for every task in todo_list
    print(f'{index+1} {task}') #prints the task

# number_of_tasks = len(todo_list)
print(f'You have {len(todo_list)} tasks to complete')