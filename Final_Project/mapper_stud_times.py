#!/usr/bin/python

import sys

sys.stdin.readline()  # to skip header in csv file

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 19:
        author_id = data[3]
        add_at = data[8]
        #print add_at
        (date,time) = add_at.strip().split()
        hr = time[:2]
        print "{0}\t{1}".format(author_id, hr)
