# Write an infinite loop that prints 1, 2, 3, 4, 5, 6, 7, 8, ......   Press the red stop button to stop your program.
#import the time module. (i looked up how to slow down the counting process)
import time
#define the number variable
number = 1
#create an infinite loop using while true
while True:
    print(number)
    number+=1 # += is syntax for incrementing up by the defined amount.
    time.sleep(1) #delays the count by 1 second per loop.