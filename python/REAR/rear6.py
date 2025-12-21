import sys, queue, math, random

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)



#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs = f.readfasta(lines)
# print(n, names, strings)
lines.append('')
assert len(lines)/3 == len(lines)//3


minn = 1000
def allperms(L1, L2, n):
    if L1 == L2:
        print('done in ', n)
        return
    print('---')
    print(L1)
    print(L2)
    print(n)
    if n > 10:
        #print('exit')
        return -1
    global minn
    l = len(L1)
    assert len(L2) == l
    for i in range(l):
        for j in range(i+1,l):
            TL = L1.copy()
            if i == j:
                continue
            a = TL[i:j+1]
            TL = TL[:i] + a[::-1] + TL[j+1:]
            allperms(TL, L2, n + 1)


for i in range(len(lines)//3):
    a = [int(x) for x in lines[i*3].split(' ')]
    b = [int(x) for x in lines[i*3+1].split(' ')]
    print("a:   ", a)
    print("b:   ", b)

    res = allperms(a, b, 1)
    sys.exit()