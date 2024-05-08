import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import copy

# https://rosalind.info/problems/ba1a

#
# #
#


def getkmers(s1, k):
    res = []
    for i in range(len(s1) - k + 1):
        res.append(s1[i:i+k])
    return res

def diffn(s1, s2, n):
    assert len(s1) == len(s2)
    diffs = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffs += 1
    if diffs <= n:
        return True
    return False


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs, qual = f.readfastq(lines[1:])

k, d = map(int, lines[0].split())
seqs = lines[1:]

res = []
seen = set()
for l in seqs:
    oldres = copy.deepcopy(res)
    res = []
    kmers = getkmers(l, k)
    for kmer in kmers:
        if len(oldres) == 0:
            res.append(kmer)
        else:
            for r in oldres:
                if not diffn(r, kmer, d) and not kmer in seen:
                    res.append(kmer)
                    seen.add(kmer)


print(seen)
print(' '.join(res))
