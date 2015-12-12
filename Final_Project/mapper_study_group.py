#!/usr/bin/python

import sys

sys.stdin.readline()  # to skip header in csv file

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 19:
        author_id = data[3]
        node_type = data[5]
        if node_type == 'question':
            node_id = data[0]
        else:   # answer or comment
            node_id = data[6]    # parent id

        print "{0}\t{1}".format(node_id, author_id)
