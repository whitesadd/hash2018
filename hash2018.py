'''
Created on the 19th of February, 2018

@author: 'Per Kata Ad Astra' Team
'''
import sys

numberOfRows = 0
numberOfColumns = 0
numberOfVehicles = 0
numberOfRides = 0
perRideBonus = 0
numberOfSimSteps = 0

def parse_input(inputFile):

    f = open(inputFile,"r")

    ## Read one line
    #line = f.readline()
    #print(line)

    ## Read all lines in file
    #for line in f:
    #    print(line)

    listWithAllLines = f.readlines()
    firstRow = listWithAllLines[0].split()
    numberOfRows = int(firstRow[0])
    numberOfColumns = int(firstRow[1])
    numberOfVehicles = int(firstRow[2])
    numberOfRides = int(firstRow[3])
    perRideBonus = int(firstRow[4])
    numberOfSimSteps = int(firstRow[5])
    f.close()


def dump_output():

    f = open("file.out","w")

    ## Write stuff
    f.write("%s\n" % "Some stuff to write in out file")

    f.close()


def get_dist(rs, cs, re, ce):
    assert(isinstance(rs, int))
    assert(isinstance(cs, int))
    assert(isinstance(re, int))
    assert(isinstance(ce, int))
    return abs(rs - re) + abs(cs - ce)

def main():
    print("!!!!Google Hash 2018!!!!")
    if len(sys.argv) >= 2:
      fileInput = sys.argv[1]
    else:
      fileInput = "a_example.in"
      parse_input(fileInput)


if __name__ == '__main__':
    main()
