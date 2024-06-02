import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
from collections import defaultdict

# https://rosalind.info/problems/ba1e

#
# #
#


def getkmers(s1, k):
    d = defaultdict(int)
    res = set()
    for i in range(len(s1) - k + 1):
        kmer = s1[i : i + k]
        assert len(kmer) == k
        d[kmer] += 1
        res.add(kmer)
    return sorted(list(res)), d


def findspan(s1, patt):
    l = len(patt)
    b = s1.find(patt)
    e = s1.rfind(patt)
    return e - b + l


assert findspan("AABAA", "AA") == 5
assert findspan("AAA", "AA") == 3


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs, qual = f.readfastq(lines[1:])

assert len(lines) == 2

k, L, t = map(int, lines[1].split())

seq = lines[0]
assert len(seq) >= L

kmers, freq = getkmers(seq, k)

res = []
for km in freq:
    if freq[km] >= t:
        if findspan(seq, km) <= L:
            res.append(km)

print(' '.join(res))
