

def main():
    print('Bus fare calculator!') #title of program for user readability
    # variable to determine the total cost of regular/rush fare rides. Calls bus_ride_cost_calculator function. Uses regular/rush argument to send to calculator function
    total_regular_cost = bus_ride_cost_calculator('regular')
    total_rush_cost = bus_ride_cost_calculator('rush')

#function to calculate the cost of rides
#uses fare_type parameter to determine if it is rush/regular
def bus_ride_cost_calculator(fare_type):
    number_of_rides = int(input(f'How many times did ride the bus paying {fare_type} fares?: '))
    bus_fare = float(input(f'What is the price of one {fare_type} bus ticket?: $'))
    #multiiply variables to determine total_cost
    total_cost = bus_fare * number_of_rides

    print(f'You rode the bus {number_of_rides} times and each ride costs ${bus_fare:.2f}')
    print(f'Your total bus fairs are ${total_cost:.2f}')
    #return total_cost to main()
    return total_cost

main()