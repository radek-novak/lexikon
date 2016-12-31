#!/usr/bin/python
# coding: utf-8

import sys
from pattern.de import gender

gender_map = {
    'f': 'die',
    'm': 'der',
    'n': 'das'
}

def main(argument):
    return gender_map[gender(argument)]

if __name__ == '__main__':
    # print 'This program is being run by itself with %s arguments' % (len(sys.argv) - 1)
    print main(sys.argv[1])
else:
    print 'I am being imported from another module'
