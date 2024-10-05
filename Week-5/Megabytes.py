#create main() function
def main():
    mega = float(input('How many megabytes is the file?: ')) #get user input to define the amount of megabytes the file is.
    b_bytes = mg_to_b(mega) #define the bytes variable with a call to a function below
    print(f'{mega} megabytes is equal to {b_bytes} bytes of date. ') #print the conversion message.

#creat a function to then define the b_bytes variable
def mg_to_b(mega):
    b = mega * 1000000 #equation to convert megabytes to bytes
    return b #this returns to main() function to then define b_bytes

main() #runs the main() function resulting in a print of the conversion

