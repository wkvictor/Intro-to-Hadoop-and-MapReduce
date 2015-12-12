#!/usr/bin/python

import sys

old_id = None
author_list = []

for line in sys.stdin:
    
    data_mapped = line.strip().split('\t')

    if len(data_mapped) != 2:
        continue

    this_id, author_id = data_mapped

    """ Notice checking old_id!!!  """
    if old_id and this_id != old_id:   # encounter new id
        print "{0}\t{1}".format(old_id, author_list)
        old_id = this_id
        author_list = [author_id]
 
    else:        # first initialization or encounter old id
        old_id = this_id
        author_list.append(author_id)
        

            
if old_id:    # print last one
    print "{0}\t{1}".format(old_id, author_list)



