#!/usr/bin/python

import sys

IP_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    ip = data_mapped[0]

    try:
        IP_dict[ip] += 1
    except KeyError:
        IP_dict[ip] = 1


try:
    print "Number of hits made by 10.99.99.186:", IP_dict['10.99.99.186']
except:
    print "Required key does not exist in current log."


print "IP", "\t", "Number of hits"
for ip in IP_dict:
    print ip, "\t", IP_dict[ip]

    
