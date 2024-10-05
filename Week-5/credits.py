
def main():
    credits_completed = 34 #define credits_completed variable
    college = 'MPLS' #define college
    report(credits_completed, college) #run the report function

def report(cr, col): #cr is assigned to credits_completed, col is assigned to college variable
    print('Your school is', col) #print with the col/college variable
    print(f'You need {60 - cr} credits to graduate') #print with the cr/credits_completed variable

main()