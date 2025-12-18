import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
from collections import defaultdict
from functools import cache

# https://rosalind.info/problems/motz

#
# #
#


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs, qual = f.readfastq(lines[1:])

s1 = ''.join(lines[1:])

b = {'A': 'U', 'U': 'A', 'G':'C', 'C':'G'}



D = {}

def motzkin(s, n):
    if len(s) == 0 or len(s) == 1:
        return 1
    if s in D:
        return D[s]
    res = 0
    for m in range(len(s)):
        if b[s[0]] == s[m]:
            #print(m)
            s1 = s[1:m]
            s2 = s[m+1:]
            n += 1
            res +=  motzkin(s1,n) * motzkin(s2,n)
    res += motzkin(s[1:],n)
    D[s] = res
    return res

assert motzkin('AUAU', 0) == 7

res = motzkin(s1,0)
print(res % 1000000)