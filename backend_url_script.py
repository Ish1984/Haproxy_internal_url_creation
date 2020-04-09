#!/usr/bin/env python
import re
file1 = open('$Region.txt', 'r')
Lines = file1.readlines()
for line in Lines:
    RawData= re.findall(r"'(.*?)'",line)
    RawData.reverse()
    RawData.append("tpp.tsysecom.com")
    print '%s' % '.'.join(map(str, RawData))
