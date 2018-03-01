class Ride:
    def __init__(self, ride_string):
        inputs = ride_string.split(' ')
        self.start = [int(inputs[0]), int(inputs[1])]
        self.finish = [int(inputs[2]), int(inputs[3])]
        self.start_time = int(inputs[4])
        self.end_time = int(inputs[5])

    def __str__(self):
        ret = "{} -> {}: start={}, end={}".format(
            self.start,
            self.finish,
            self.start_time,
            self.end_time)
        return ret

class Car:
    def __init__(self, order_string):
        self.orders = order_string.split(' ')[1:]
        self.pos = [0, 0]


class City:
    def __init__(self, input_file):
        self.rides = {}
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
                self.rides[cnt] = Ride(ride.strip('\n'))
                cnt += 1

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
