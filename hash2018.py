'''
Created on the 19th of February, 2018

@author: 'Per Kata Ad Astra' Team
'''
import sys
import parser
from queue import Queue


def find_best_ride(car, rides, current_tick):
    best_ride = None
    best_score = 0

    for ride in rides.values():
        score = car.evaluate_ride(ride, current_tick)
        if score > best_score:
            best_ride = ride
            best_score = score

    return best_ride


def strategy(city, out_name):
    car_queue = Queue()
    parser.Car.car_queue = car_queue

    for tick in range(city.numberOfSimSteps):
        for car in city.cars:
            car.tick()

        while(not car_queue.empty()):
            car = car_queue.get()
            ride = find_best_ride(car, city.rides, tick)
            if ride is None:
                break

            car.add_ride(ride, tick)
            del city.rides[ride.ride_number]

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
                 "d_metropolis.in",
                 "e_high_bonus.in"]
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
