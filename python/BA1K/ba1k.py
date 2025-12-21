import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
from collections import defaultdict
from functools import cache
import itertools as it

# https://rosalind.info/problems/ba1i

#
# #
#


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs, qual = f.readfastq(lines[1:])

assert len(lines) == 2

s1 = lines[0]
k = int(lines[1])

kms = s.kmers(k)

res = []
for km in sorted(kms):
    cnt = 0
    for i in range(len(s1)-k+1):
        if s1[i:i+k] == km:
            cnt +=1
    res.append(cnt)
    print(km, cnt)

print(' '.join(list(map(str, res))))