#!/usr/bin/python

import sys

file_dict = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue
    
    page = data_mapped[1].strip('http://www.the-associates.co.uk')

    if page == '/' or page == '':
        continue

    try:
        file_dict[page] += 1
    except KeyError:
        file_dict[page] = 1

highest_page = ''
highest_hit = 0

for page in file_dict:
    if file_dict[page] > highest_hit:
        highest_hit = file_dict[page]
        highest_page = page

print "Most popular file's pathname:", highest_page
print "Number of occurence:", highest_hit

    
