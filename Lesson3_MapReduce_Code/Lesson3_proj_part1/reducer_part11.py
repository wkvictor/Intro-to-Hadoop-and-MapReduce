#!/usr/bin/python

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

import sys

old_item = None
cost_total = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    this_item, this_cost = data_mapped

    if old_item != None and this_item != old_item:  # when encounter new item
        print old_item, "\t", cost_total
        old_item = this_item
        cost_total = 0
        cost_total += float(this_cost)
    else:
        old_item = this_item
        cost_total += float(this_cost)

if old_item != None:    # print last item's total
    print old_item, "\t", cost_total

