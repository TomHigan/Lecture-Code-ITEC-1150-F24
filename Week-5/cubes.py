#creat main() function to determine how many numbers to cube
def main():
    for number in range(11): #run the loop variable number 11 times
        c = cube(number) #define c with the function cube() below. number is taken from the loop variable, currently 0-10
        print(c) #print results

#function to define c variable above
def cube(value):
    cubed_value = value ** 3 #this takes the value and multiplies it by itself 3 times. The value is currently the number loop variable from above.
    return cubed_value #this is the value that is then assigned to the cube() function and is used to define c

main()