#!/usr/bin/python

import sys

file_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    page = data_mapped[1]

    if page == '/':
        continue

    try:
        file_dict[page] += 1
    except KeyError:
        file_dict[page] = 1

print
try:
    print "Number of hits made to the page /assets/js/the-associates.js:", file_dict['/assets/js/the-associates.js']
except:
    print "Required key does not exist in current log."

print
print "Page", "\t", "Number of hits"
for page in file_dict:
    print page, "\t", file_dict[page]

    
