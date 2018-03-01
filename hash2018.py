'''
Created on the 19th of February, 2018

@author: 'Per Kata Ad Astra' Team
'''
import sys
import parser


def dump_output(f_name):

    f = open(f_name,"w")

    ## Write stuff
    f.write("%s\n" % "Some stuff to write in out file")

    f.close()

def find_nearest_car(ride, cars):
    nearest_car = None
    nearest_dist = 9999999999999999

    for car in cars:
        dist = parser.get_dist(ride.start, car.pos)
        if dist < nearest_dist and car.available_in == 0:
            nearest_car = car
            nearest_dist = dist

    return nearest_car


def strategy(city, out_name):
    rides = city.rides.values()
    rides = sorted(rides, key=lambda ride: ride.start_time)

    for tick in range(city.numberOfSimSteps):
        for car in city.cars:
            car.tick()

        while len(rides):
            ride = rides[0]
            car = find_nearest_car(ride, city.cars)
            if car is None:
                break

            car.add_ride(ride, tick)
            rides.pop(0)

    with open(out_name, 'w') as f:
        for car in city.cars:
            f.write("%s\n" % car.__str__())


def main():
    print("!!!!Google Hash 2018!!!!")
    if len(sys.argv) >= 2:
        fileInput = sys.argv[1]
        out_name = sys.argv[2]
    else:
        fileInput = "a_example.in"

    city = parser.City(fileInput)

    # Access the parameters
    print(city.numberOfRows)
    print(city.numberOfColumns)
    print(city.numberOfVehicles)
    print(city.numberOfRides)
    print(city.perRideBonus)
    print(city.numberOfSimSteps)

    # Access the first route
    # print(city.rides[0])

    ## Print the entire input
    #print(city)

    strategy(city, out_name)
if __name__ == '__main__':
    main()
