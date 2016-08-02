#!/usr/bin/python

import sys

list_of_ips = {}

for line in sys.stdin:
	line = line.strip()
	list_of_ips[line]=line
	#print line

#print "++++"

s = sorted(list_of_ips, key=lambda ip: long(''.join(["%02X" % long(i) for i in ip.split('.')]), 16))

for key in s:
	print "%s" % key


