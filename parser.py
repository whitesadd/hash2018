class Ride:
    def __init__(self, ride_string):
        inputs = ride_string.split(' ')
        self.start = [inputs[0], inputs[1]]
        self.finish = [inputs[2], inputs[3]]
        self.start_time = inputs[4]
        self.end_time = inputs[5]


class Car:
    def __init__(self, order_string):
        self.orders = order_string.split(' ')[1:]
        self.pos = [0, 0]


def ride_factory(self, ride_input):
    rides = {}

    cnt = 0
    for ride in ride_input:
        rides[cnt] = Ride(ride)
        cnt += 1

    return rides
