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


def hamming(s1, s2):
    assert len(s1) == len(s2)
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs, qual = f.readfastq(lines[1:])


patt = lines[0]
plen = len(patt)
seq = lines[1]
hdist = int(lines[2])

res = []
for i in range(len(seq) - plen + 1):
    s1 = seq[i : i + plen]
    if hamming(s1, patt) <= hdist:
        res.append(str(i))

print(' '.join(res))
