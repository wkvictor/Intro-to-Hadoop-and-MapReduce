#!/usr/bin/python

import sys

sys.stdin.readline()  # to skip header in csv file

for line in sys.stdin:
    data = line.strip().split('\t')
    if len(data) == 19:
        node_type = data[5]
        if node_type == 'question':
            node_id = data[0]
            post_len = len(data[4])
        elif node_type == 'answer':
            node_id = data[6]    # parent id
            post_len = len(data[4])
        else:
            continue

        print "{0}\t{1}\t{2}".format(node_id, node_type, post_len)
