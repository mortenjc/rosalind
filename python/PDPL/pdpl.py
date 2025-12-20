import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
from collections import defaultdict
from functools import cache
import itertools as it
import math as m

# https://rosalind.info/problems/ba1i

#
# #
#


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs, qual = f.readfastq(lines[1:])

assert len(lines) == 1

L = lines[0].split()
L = list(map(int, L))
L=sorted(L)

def deltax(lst):
    DX = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i == j:
                continue
            if lst[i]-lst[j] >= 0:
                DX.append(lst[i]-lst[j])
    return sorted(list(DX))


def dists(y, x):
    res = [abs(y-a) for a in x]
    return res



# X and L are lists
sols = []
def solve(L, X, width):
    if L == []:
        sols.append(X.copy())
        return X
    y = max(L)

    res = dists(y,X)
    if all(e in L for e in res):
        X.append(y)
        for e in res:
            L.remove(e)
        solve(L, X, width)
        X.remove(y)
        for e in res:
            L.append(e)

    res = dists(width-y,X)
    if all(e in L for e in res):
        X.append(width-y)
        for e in res:
            L.remove(e)
        solve(L, X, width)
        X.remove(width-y)
        for e in res:
            L.append(e)
    #print('no possibilities')
    return sols


width = max(L)
L.remove(width)
X = [0, width]
res = solve(L, X, width)

for r in res:
    print(' '.join(map(str, sorted(r))))
    print()

