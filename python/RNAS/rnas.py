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

s1 = ''.join(lines)

def wmatch(c1, c2):
    b = {'A': 'U', 'U': 'A', 'G':'C', 'C':'G'}
    return b[c1] == c2


def umatch(c1, c2):
    b2 = {'U':'G', 'G':'U'} 
    if c1 in ['U', 'G'] and c2 in ['U','G'] and b2[c1] == c2:
        return True
    return False

D = {}

def motzkin(s, n):
    if len(s) == 0 or len(s) == 1:
        return 1
    if s in D:
        return D[s]
    res = 0
    for m in range(len(s)):
        if (wmatch(s[0], s[m]) or umatch(s[0], s[m])) and m>=4:
            s1 = s[1:m]
            s2 = s[m+1:]
            n += 1
            res +=  motzkin(s1,n) * motzkin(s2,n)
    res += motzkin(s[1:],n)
    D[s] = res
    return res


print(s1)
res = motzkin(s1,0)
print(res)