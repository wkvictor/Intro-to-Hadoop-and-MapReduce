#!/usr/bin/python

import sys

high_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    store = data_mapped[0]
    cost = float(data_mapped[1])

    if store in high_dict.keys():
        if cost > high_dict[store]:
            high_dict[store] = cost
    else:
        high_dict[store] = cost

print "Reno", "\t", high_dict['Reno']
print "Toledo", "\t", high_dict['Toledo']
print "Chandler", "\t", high_dict['Chandler']

    
