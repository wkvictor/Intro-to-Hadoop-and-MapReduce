#!/usr/bin/python

import sys
import re
import csv

p = re.compile(ur'[^\s+\,\.\!\?\:\;\"\(\)\<\>\#\$\=\-\/]+')
reader = csv.reader(sys.stdin, delimiter='\t')
next(reader, None)   # skip header
for line in reader:
    if len(line) >= 5:
        node = line[0]
        body = line[4]
        words = [word.lower() for word in re.findall(p,body)]
        for word in words:
            print "{0}\t{1}".format(word, node)
