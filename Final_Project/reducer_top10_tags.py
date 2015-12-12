#!/usr/bin/python

import sys

old_tag = None
tag_list = []
tag_cnt = 0

for line in sys.stdin:

    data_mapped = line.strip().split('\t')

    if len(data_mapped) != 2:
        continue

    this_tag = data_mapped[0]
    #print this_tag
    
    if old_tag and old_tag!=this_tag:
        tag_list.append((old_tag,tag_cnt))
        tag_list.sort(key=lambda x: x[1])
        if len(tag_list) > 10:
            tag_list.pop(0)

        old_tag = this_tag
        tag_cnt = 0
        tag_cnt += 1
       
    else:
        old_tag = this_tag
        tag_cnt += 1
    
if old_tag:
    tag_list.append((old_tag,tag_cnt))
    tag_list.sort(key=lambda x: x[1])
    if len(tag_list) > 10:
        tag_list.pop(0)

print "tag\tfrequency"
for tag in tag_list:
    print "{0}\t{1}".format(tag[0], tag[1])



