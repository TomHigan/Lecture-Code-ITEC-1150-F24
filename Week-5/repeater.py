
def main():
    string = input('Please enter a string: ') #get user input
    repeat = int(input('How many times should we repeat it? ')) #user input to then repeat above string
    result = string_repeater(string, repeat) #define th result variable with a function to run below.
    print(result)

#function used to define the result variable
def string_repeater(text, n): #(text,n) is correlated to the above (string,repeat) values
    repeated_string = text * n #again string * repeat variables from above.
    return repeated_string #value then returned to the result variable

main()