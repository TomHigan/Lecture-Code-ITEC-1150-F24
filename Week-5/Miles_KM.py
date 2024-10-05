#begnin the main() function
def main():
    miles = float(input('Please enter a number of miles: ')) #get user input and assign to the miles variable
    kilometers = miles_to_km(miles) #define the kilometers variable with a call to a function
    print(f'{miles} miles is equal to {kilometers} kilometers. ') #print the results of the functions

#function used to define the kilometers variable
def miles_to_km(miles):
    km = miles * 1.60934 #variable and equation to convert km to miles
    return km #this is what the function returns to the main() function to then help define the kilometers variable

main()