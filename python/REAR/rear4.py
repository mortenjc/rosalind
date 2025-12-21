import sys, queue, math, random

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)


# reverse sublist starting from (including) begin
# and ending with (including) end
def reverse(s, begin, end):
    mid = s[begin:end+1]
    return s[:begin] + mid[::-1] + s[end+1:]
assert reverse([1,2,3,4,5], 1, 3) == [1, 4, 3, 2, 5]


def bkpts(s1):
    bps = 0
    rev = False
    s = [0] + s1 + [len(s1) + 1]
    for i in range(len(s)-1):
        diff = s[i+1] - s[i]
        if abs(diff) != 1:
            bps +=1
        else:
            if diff < 0:
                rev = True
    return bps, rev

assert bkpts([1,2,3]), (0, False)
assert bkpts([1,3,2]), (2, True)


def isordered(s1):
    for i in range(len(s1)):
        if s1[i] != i+1:
            return False
    return True

def mkmap(s1, s2):
    d = {}
    for i in range(len(s1)):
        d[s1[i]] = i+1
    for i in range(len(s1)):
        s2[i] = d[s2[i]]
    return s2

assert mkmap([1,2,3],[3,2,1]) == [3,2,1]
assert mkmap([2,3,1],[3,2,1]) ==[2,1,3]

#print(mkmap([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]))

def allperms(s1):
    l = len(s1)
    ibp, _ = bkpts(s1)
    for i in range(l-1):
        for j in range(i+1, l):
            ns = reverse(s1, i, j)
            n, _ = bkpts(ns)
            if n < ibp:
                #print(i,j)
                return ns
    return []


def findrevs(s1):
    revs = 0
    res = s1
    while (True):
        n, _ = bkpts(res)
        if n == 0:
            break
        res = allperms(res)
        revs +=1
    #print(f'{revs} : {s1} -> {res}')
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




for i in range(len(lines)//3):
    a = [int(x) for x in lines[i*3].split(' ')]
    b = [int(x) for x in lines[i*3+1].split(' ')]
    m = mkmap(a, b)

    ba, bba = bkpts(a)
    bb, bbb = bkpts(b)
    # print("a:   ", a)
    # print("b:   ", b)
    # print(ba)
    # print(bb)
    
    # print("map: ", m)
    revs = findrevs(m)
    if not isordered(a):
        res = revs - 1
    else:
        res = revs

    if bba == False and bbb == False:
        print(res)
    elif bba == True and bbb == True:
        print(revs)
    else:
        print(res)

#    print(revs, res)
