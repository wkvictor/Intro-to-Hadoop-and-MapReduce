#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split()
    if len(data) == 10:
        ip = data[0]
        page = data[6]
        print "{0}\t{1}".format(ip, page)

