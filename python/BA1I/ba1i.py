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

# return list of all k-mers of length l
def kmers(l):
    lst = it.combinations_with_replacement('ATGC', l)
    a = [ ''.join(x) for x in lst]
    #print(a)
    return a

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
# print('-------')
# print(dna)
# print(k, d)
# print('-------')

kms = kmers(k)
res = {}
allkm = []


for km in kms:
    perms = it.permutations(km)
    a = [''.join(x) for x in perms]
    for x in a:
        if x not in allkm:
            allkm.append(x)

for km in allkm:
    cnt = 0
    idx = []
    for j in range(len(dna)-len(km)):
        s1 = dna[j:j+k]
        if mismatches(s1, km) <= d:
            idx.append(j)
            cnt += 1
    #print(f'mismatches between {dna} and {km}: {cnt} ({idx})')
    if cnt != 0:
        res[km] = cnt

# print(res)
maxval = max(res.values())
m = [x for x in res if res[x] == maxval]
print(' '.join(m))
