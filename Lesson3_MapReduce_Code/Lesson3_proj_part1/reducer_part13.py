#!/usr/bin/python

import sys

sales_total = 0.0
sales_count = 0

for line in sys.stdin:
    data_mapped = line.strip()
    if len(data_mapped) != 1:
        continue

    sales = float(data_mapped)
    sales_total += sales
    sales_count += 1

print "Total number of sales", "\t", sales_count
print "Total sales value", "\t", sales_total
    
