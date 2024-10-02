# Write a loop that prints all the dates in January. So your program will print
# January 1
# January 2
# January 3
# ... more dates here ...
# January 30
# January 31
import time
for day in range(1,32): #loop from 1 to 31
    # print January then the day variable
    print(f'January {day}')
    time.sleep(1)

