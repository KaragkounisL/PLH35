#!/usr/bin/python3
# Script to split the family and domain name from the Netlab360 list -- Discard the time data
with open('netlab360_list.txt', 'r') as handle:
    lines = handle.readlines()
with open('dga.txt', 'w+') as whandle:
    for i in range(18, len(lines)):
        whandle.write(lines[i].split()[0]+'\t'+lines[i].split()[1]+'\n')
