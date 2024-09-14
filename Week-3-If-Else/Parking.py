parking_time = float(input('How many hours have you parked: '))
#max parking is 2 hours

if parking_time >= 2:
    print('Warning you should move your car.')
#print how many hours over
    time_over = parking_time - 2
    print('You are ' + str(time_over) + ' hours over the limit.')
else:
    print('You still have time!')
#print how many hours are left
    time_left = 2 - parking_time
    print('You have ' + str(time_left) + ' hours left.')