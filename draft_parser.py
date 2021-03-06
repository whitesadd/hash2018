def get_dist(pos1, pos2):
    rs = pos1[0]
    cs = pos1[1]
    re = pos2[0]
    ce = pos2[1]
    assert(isinstance(rs, int))
    assert(isinstance(cs, int))
    assert(isinstance(re, int))
    assert(isinstance(ce, int))
    return abs(rs - re) + abs(cs - ce)

class Ride:
    def __init__(self, ride_number, ride_string):
        inputs = ride_string.split(' ')
        self.start = [int(inputs[0]), int(inputs[1])]
        self.finish = [int(inputs[2]), int(inputs[3])]
        self.start_time = int(inputs[4])
        self.end_time = int(inputs[5])
        self.ride_number = ride_number
        self.distance = get_dist(self.start, self.finish)

    def __str__(self):
        ret = "{} -> {}: start={}, end={}".format(
            self.start,
            self.finish,
            self.start_time,
            self.end_time)
        return ret

class Car:
    def __init__(self):
        self.pos = [0, 0]
        self.available_in = 0
        self.rides = []

    def tick(self):
        if self.available_in > 0:
            self.available_in -= 1

    def add_ride(self, ride, current_tick):
        # Distance to the pickup point
        n = get_dist(self.pos, ride.start)

        # Wait time
        w = 0
        if current_tick + n < ride.start_time:
            w = ride.start - current_tick + n

        m = ride.distance + w + n

        if current_tick + m <= ride.end_time:
            self.available_in = m
            self.rides.append(ride.ride_number)

    #def __str__(self):
    #    '{} {}'.format(len(self.

class City:
    def __init__(self, input_file):
        self.rides = {}
        self.cars = []
        with open(input_file,"r") as f:

            ## Read one line
            #line = f.readline()
            #print(line)

            ## Read all lines in file
            #for line in f:
            #    print(line)

            ride_input = f.readlines()
            firstRow = ride_input[0].strip('\n').split(' ')
            self.numberOfRows = int(firstRow[0])
            self.numberOfColumns = int(firstRow[1])
            self.numberOfVehicles = int(firstRow[2])
            self.numberOfRides = int(firstRow[3])
            self.perRideBonus = int(firstRow[4])
            self.numberOfSimSteps = int(firstRow[5])

            cnt = 0
            for ride in ride_input[1:]:
                self.rides[cnt] = Ride(cnt, ride.strip('\n'))
                cnt += 1

            for x in range(self.numberOfVehicles):
                self.cars.append(Car())

    def __str__(self):
        string = ""
        string += str(self.numberOfRows)
        string += " " + str(self.numberOfColumns)
        string += " " + str(self.numberOfVehicles)
        string += " " + str(self.numberOfRides)
        string += " " + str(self.perRideBonus)
        string += " " + str(self.numberOfSimSteps)

        string += "\n"
        for ride in self.rides.values():
            string += ride.__str__() + '\n'

        return string
