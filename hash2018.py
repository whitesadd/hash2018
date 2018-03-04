'''
Created on the 19th of February, 2018

@author: 'Per Kata Ad Astra' Team
'''
import sys
import parser


def dump_output(f_name):

    f = open(f_name, "w")

    # Write stuff
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
    fileInputs = []
    if len(sys.argv) >= 2:
        fileInputs.append((sys.argv[1],
                          sys.argv[2]))
    else:
        files = ["a_example.in",
                 "b_should_be_easy.in",
                 "c_no_hurry.in",
                 "d_metropolis.in"]
        for f in files:
            out_file = 'out/' + f.split('.')[0] + '.out'
            in_file = f
            fileInputs.append((in_file, out_file))

    for in_out in fileInputs:
        in_file = in_out[0]
        out_file = in_out[1]
        print("Optimizing for", in_file, "...")
        city = parser.City(in_file)
        strategy(city, out_file)
        print("Done, results written to", out_file)

if __name__ == '__main__':
    main()
