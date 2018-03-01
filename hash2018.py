'''
Created on the 19th of February, 2018

@author: 'Per Kata Ad Astra' Team
'''

def parse_input():

    f = open("file.in","r")

    ## Read one line
    line = f.readline()
    print(line)

    ## Read all lines in file
    for line in f:
        print(line)

    f.close()


def dump_output():

    f = open("file.out","w")

    ## Write stuff
    f.write("%s\n" % "Some stuff to write in out file")

    f.close()


def get_dist(rs, cs, re, ce):
    return abs(rs - re) + abs(cs - ce)

def main():
    print("!!!!Google Hash 2018!!!!")


if __name__ == '__main__':
    main()
