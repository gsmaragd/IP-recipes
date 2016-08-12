#!/usr/bin/python

import sys
from collections import defaultdict

counts = defaultdict(int)


#list_of_ips = {}

list_of_ips = set()


for line in sys.stdin:
    line = line.strip()
    #list_of_ips[line] = line
    list_of_ips.add(line)
    counts[line] += 1
    print line

print "++++"

s = sorted(list_of_ips, key=lambda ip: long(''.join(["%02X" % long(i) for i in ip.split('.')]), 16))

for key in s:
    print str(key) + " " + str(counts[key])


