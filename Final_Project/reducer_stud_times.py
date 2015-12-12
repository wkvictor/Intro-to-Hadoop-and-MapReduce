#!/usr/bin/python

import sys


old_id = None
hr_dict = {}

for line in sys.stdin:
    
    data_mapped = line.strip().split('\t')

    if len(data_mapped) != 2:
        continue

    this_id, this_hr = data_mapped

    """ Notice checking old_id!!!  """
    if old_id and this_id != old_id:   # encounter new id
        hr_max = max(hr_dict.values())   # check old_id, ow values do not exist!
        for hr in hr_dict:
            if hr_dict[hr] >= hr_max:
                print "{0}\t{1}".format(old_id, hr)
        old_id = this_id
        hr_dict = {}    # reset
        hr_dict[this_hr] = 1  # initialize now 
 
    else:        # first initialization or encounter old id
        old_id = this_id   # Notice to update key now!!
        try:
            hr_dict[this_hr] += 1
        except KeyError:
            hr_dict[this_hr] = 1

            
if old_id:    # print last one
    hr_max = max(hr_dict.values())
    for hr in hr_dict:
        if hr_dict[hr] >= hr_max:
            print "{0}\t{1}".format(old_id, hr)
