'''
Created on the 19th of February, 2018

@author: 'Per Kata Ad Astra' Team
'''
import sys
import parser


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
      city = parser.City(fileInput)


if __name__ == '__main__':
    main()
