#!/usr/bin/env python3
#

import draft_parser

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


file_name = "e_high_bonus.in"
fh = open(file_name)


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

city = parser.City(file_name)
rides = city.rides.values()

dist = []
for i in rides:
    dist.append(get_dist(i.start, i.finish))

arraySortedRides = []

for item in range(len(dist)):
    maxDist = 0
    maxIndex = 0
    Index = 0
    for d in dist:
        if d > maxDist:
            maxDist = d
            maxIndex = Index
        Index += 1
    arraySortedRides.append(maxIndex)
    dist[maxIndex] = 0

#print(arraySortedRides)

for i in range(int(cars)):
    print('1',arraySortedRides[i])
