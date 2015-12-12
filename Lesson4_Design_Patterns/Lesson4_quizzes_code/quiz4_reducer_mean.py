#!/usr/bin/python

import sys

weekday_total = {'Monday':[0.0, 0], 'Tuesday':[0.0, 0], 'Wednesday':[0.0, 0],\
                'Thursday':[0.0, 0], 'Friday':[0.0, 0], 'Saturday':[0.0, 0], 'Sunday':[0.0, 0]}

for line in sys.stdin:
    
    data_mapped = line.strip().split(":")
    
    if len(data_mapped) != 2:
        continue

    wd = data_mapped[0]
    val = float(data_mapped[1])

    weekday_total[wd][0] += val
    weekday_total[wd][1] += 1


for wd in weekday_total.keys():
    if weekday_total[wd][1]:
        print "{0}\t{1}".format(wd, weekday_total[wd][0] / weekday_total[wd][1])
    
