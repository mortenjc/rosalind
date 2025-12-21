import sys, queue, math, random

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)


def transform(L1, L2):
    D = {}
    assert len(L1) == len(L2)
    for i in range(len(L1)):
        ic = i + 1
        D[L1[i]] = ic
    #print(D)
    # for x in L2:
    #     print(f'{x} -> {D[x]}')
    res = [ D[x] for x in L2]
    #print(res)
    return res


def revsort(L):
    revs = 0
    #print(L)
    R = sorted(L.copy())
    for i in range(len(L)):
        j = L.index(i+1)
        if i != j:
            revs += 1
            # print(i, j)
            # print(L[:i])
            # print(list(reversed(L[i: j+1])))
            # print(L[j+1:])
            L = L[:i] + list(reversed(L[i: j+1])) + L[j+1:]
            print(L)
        if L == R:
            break
    return revs


#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs = f.readfasta(lines)
# print(n, names, strings)
lines.append('')
assert len(lines)/3 == len(lines)//3



r = [6, 1, 2, 3, 4, 5]
res = revsort(r)
print(res)
sys.exit()

for i in range(len(lines)//3):
    a = [int(x) for x in lines[i*3].split(' ')]
    b = [int(x) for x in lines[i*3+1].split(' ')]
    print("a:   ", a)
    print("b:   ", b)

    bt = transform(a,b)
    print("bt:  ", bt)
    # #ra = revsort(a)
    rb = revsort(bt)
    print(f'reversals: {rb}')
    rbr = revsort(list(reversed(bt)))
    print(f'reversals: {rbr}')
    print()

