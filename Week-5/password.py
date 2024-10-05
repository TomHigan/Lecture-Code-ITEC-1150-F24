#function to check the length of the password
def check_pw_length(password): #nest password variable in side the check_pw_length function
    if len(password) >= 8: #create an if statement that checks the length of the password variable
        return True #states that if the above is true to return true
    else:
        return False #if the above is not true then return false.

def main():
    password = 'kittens' #specifically defined password variable. could use input here to have user generated results.
    if check_pw_length(password): #this is running the above function and state that if it returns true print the below statement
        print(f'The password "{password}" is long enough.')
    else: #if the above function returns false, print the below statement.
        print(f'The password "{password}" is not long enough.')

main()