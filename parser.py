class Ride:
    def __init__(self, ride_string):
        inputs = ride_string.split(' ')
        print("inputs", inputs)
        self.start = [int(inputs[0]), int(inputs[1])]
        self.finish = [int(inputs[2]), int(inputs[3])]
        self.start_time = int(inputs[4])
        self.end_time = int(inputs[5])

    def __str__(self):
        return "Hej hej"


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
            print("firstRow", firstRow)
            self.numberOfRows = int(firstRow[0])
            self.numberOfColumns = int(firstRow[1])
            self.numberOfVehicles = int(firstRow[2])
            self.numberOfRides = int(firstRow[3])
            self.perRideBonus = int(firstRow[4])
            self.numberOfSimSteps = int(firstRow[5])

            cnt = 0
            for ride in ride_input[1:]:
                print("ride", ride)
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
            print("riding!!", ride)
            string += "start: " + str(ride.start)
            string += "\n"
            string += "finish: " + str(ride.finish)
            string += "\n"
            string += "start_time: " + str(ride.start_time)
            string += "\n"
            string += "end_time: " + str(ride.end_time)
            string += "\n"
        return string
