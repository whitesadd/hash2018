#!/usr/bin/env python3
#

fh = open("e_high_bonus.in")


setting = list()
array = list()

i = 0

for x in fh:
    x = x.rstrip()
    if i == 0:
        setting = x.split(" ")
    if i >= 1:
        x = list(x)
        array.append(x)
    i += 1

cars = setting[2]

for i in range(int(cars)):
    print('1',i+1)
