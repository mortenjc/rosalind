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


def mismatches(a, b):
    assert len(a) == len(b)
    #print([1 for x in range(len(a)) if a[x] == b[x]])
    return sum(1 for x in range(len(a)) if a[x] != b[x])


assert mismatches('ATTT', 'ATTC') == 1
assert mismatches('ATTT', 'ATTT') == 0

dna = lines[0]
k,d = lines[1].split()
k = int(k)
d = int(d)


allkm = s.kmers(k)

res = {}
for km in allkm:
    cnt = 0
    idx = []
    for j in range(len(dna)-len(km)):
        s1 = dna[j:j+k]
        if mismatches(s1, km) <= d:
            cnt += 1
    res[km] = cnt


maxkm = {}
for km in allkm:
    maxkm[km] = res[km] + res[tb.revcompl(km)]

maxval = max(maxkm.values())

print(' '.join([x for x in maxkm if maxkm[x]==maxval]))
