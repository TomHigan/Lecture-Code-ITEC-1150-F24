# to donate blood, you must be 17 or older, and weight 118lbs or more

#interacting with user
def main():
    age = int(input('Enter your age in years: '))
    weight = int(input('Enter your weight to the nears pound: '))
    # call function to decide if person is eligible
    eligible = check_donor_eligibility(age,weight)
    # use results - return value - to print user a message
    if eligible:
        print('You are eligible to donate!')
    else:
        print('Sorry, you are not eligible to donate.')

#uses user input to determine eligibility
def check_donor_eligibility(age,weight): #parameters age and weight are pulled from main function
    if age >= 17 and weight >= 110:
       return True #indicates that the user is eligible
    else:
        return False #indicates that the user is not eligible

main()