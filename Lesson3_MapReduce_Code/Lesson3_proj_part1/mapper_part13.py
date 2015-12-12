#!/usr/bin/python

"""
This script implements a mapper
to print out cost
"""

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        date, time, store, item, cost, payment = data
        print "{0}".format(cost)
