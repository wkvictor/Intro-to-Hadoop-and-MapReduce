#!usr/bin/python

import sys
import csv

def mapper(filename):
	reader = csv.reader(filename, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    index_dict = {}
	for line in reader:
		body = line[4].lower()
		
