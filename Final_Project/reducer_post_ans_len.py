#!/usr/bin/python

import sys


old_id = None
q_len = 0    # question length
a_len_total = 0.0 
a_len_count = 0

for line in sys.stdin:
    
    data_mapped = line.strip().split('\t')

    if len(data_mapped) != 3:
        continue

    this_id, node_type, post_len = data_mapped
    post_len = float(post_len)

    """ Notice checking old_id!!!  """
    if old_id and this_id != old_id:   # encounter new id
        if a_len_count:
            print "{0}\t{1}\t{2}".format(old_id, q_len, a_len_total/a_len_count)
        else:
            print "{0}\t{1}\t{2}".format(old_id, q_len, 0)
        old_id = this_id
        a_len_total = 0.0
        a_len_count = 0
        if node_type == 'question':
            q_len = post_len
        else:
            a_len_total += post_len
            a_len_count += 1
 
    else:        # first initialization or encounter old id
        old_id = this_id
        if node_type == 'question':
            q_len = post_len
        else:
            a_len_total += post_len
            a_len_count += 1

            
if old_id:    # print last one
    if a_len_count:
        print "{0}\t{1}\t{2}".format(old_id, q_len, a_len_total/a_len_count)
    else:
        print "{0}\t{1}\t{2}".format(old_id, q_len, 0)



