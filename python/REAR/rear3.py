import sys, queue, math, random

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)

def mkmap(l,m):
    assert len(l) == len(m)
    d = {}
    for i in range(len(l)):
        d[l[i]] = i + 1

    return [d[x] for x in m]



def GreedyReversalSort(pi):
    #print(pi)
    t = 0
    for i in range(len(pi)-1):
        j = pi.index(min(pi[i:])) # org
        if (j != i):
            pi = pi[:i] + [v for v in reversed(pi[i:j+1])] + pi[j+1:]
            #print(f"rho({i+1},{j+1}) = {pi}")
            t += 1
    return t

def GreedyReversalSort2(res, pi):
    #print(pi)
    t = 0
    for i in range(len(pi)-1):
        #j = pi.index(min(pi[i:])) # org
        j = pi.index(res[i])
        if (j != i):
            pi = pi[:i] + [v for v in reversed(pi[i:j+1])] + pi[j+1:]
            #print(f"rho({i+1},{j+1}) = {pi}")
            t += 1
    return t

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs = f.readfasta(lines)
# print(n, names, strings)
lines.append('')
assert len(lines)/3 == len(lines)//3




for i in range(len(lines)//3):
    a = [int(x) for x in lines[i*3].split(' ')]
    b = [int(x) for x in lines[i*3+1].split(' ')]
    print(a)
    print(b)
    print(GreedyReversalSort2(a,b))
