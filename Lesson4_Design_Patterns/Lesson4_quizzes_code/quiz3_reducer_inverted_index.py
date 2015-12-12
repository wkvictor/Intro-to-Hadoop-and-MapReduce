#!/usr/bin/python

import sys

word_dict = {}

for line in sys.stdin:

    data_mapped = line.strip().split('\t')

    if len(data_mapped) != 2:
        continue

    word = data_mapped[0]
    node = int(data_mapped[1])

    try:
        word_dict[word].append(node)
    except KeyError:
        word_dict[word] = [node]

try:
    print 'Number of occurence of the word "fantastic":', len(word_dict['fantastic'])
    print 'Nodes that contain the word "fantastically":', sorted(word_dict['fantastically'])
except:
    print "Keys not exist!"
    
