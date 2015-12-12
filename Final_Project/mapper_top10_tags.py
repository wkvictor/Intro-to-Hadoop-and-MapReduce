#!/usr/bin/python

import sys

sys.stdin.readline()  # to skip header in csv file

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 19:
        node_type = data[5]
        if node_type == 'question':
            tags = data[2].strip().split()
            for t in tags:
                print "{0}\t{1}".format(t, node_type)   # must print at least 2 stuffs, otherwise something goes wrong
            
