import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
from collections import defaultdict

# https://rosalind.info/problems/ba1a

#
# #
#




filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs, qual = f.readfastq(lines[1:])

s = lines[0]
k = int(lines[1])

d = defaultdict(int)

for i in range(len(s)-k+1):
    ss = s[i:i+k]
    d[ss] += 1

a = max(d.values())

res = []
for i in d:
    if d[i] == a:
        res.append(i)
print(' '.join(res))
