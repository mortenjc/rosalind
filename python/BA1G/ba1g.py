import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
from collections import defaultdict

# https://rosalind.info/problems/ba1g

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs, qual = f.readfastq(lines[1:])


s1 = lines[0]
s2 = lines[1]

dist = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        dist += 1

print(f'hamming dist: {dist}')
