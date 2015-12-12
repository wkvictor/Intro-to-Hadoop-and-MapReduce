#!/usr/bin/python
import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:

        # YOUR CODE HERE
    body = line[4]
    peri_idx = body.find('.')
    excl_idx = body.find('!')
    ques_idx = body.find('?')
    last_idx = len(body)-1
    if (peri_idx==-1 and excl_idx==-1 and ques_idx==-1) or\
       (peri_idx==last_idx and excl_idx==-1 and ques_idx==-1) or\
       (peri_idx==-1 and excl_idx==last_idx and ques_idx==-1) or\
       (peri_idx==-1 and excl_idx==-1 and ques_idx==last_idx):
        writer.writerow(line)
