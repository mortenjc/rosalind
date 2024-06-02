import sys, math, re

sys.path.append('../common')
# import toolbox as tb
import files as f

# import strings as s
from collections import defaultdict

# https://rosalind.info/problems/ba1e

#
# #
#


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs, qual = f.readfastq(lines[1:])

seq = lines[0]
res = [0]
d = defaultdict(int)
for i in range(len(seq)):
    ch = seq[i]
    d[ch] += 1
    res.append(d['G'] - d['C'])

minval = min(res)

res2 = []
for i in range(len(seq)):
    if res[i] == minval:
        res2.append(str(i))
print(' '.join(res2))
