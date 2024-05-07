import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/ba1a

#
# #
#

def match(s1, pat):
    res = []
    ls1 = len(s1)
    l = len(pat)
    assert ls1 >= l

    for i in range(ls1 - l + 1):
        if s1[i:i+l] == pat:
            res.append(str(i))
    return res


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs, qual = f.readfastq(lines[1:])

s1 = lines[1]
pat = lines[0]

r = match(s1, pat)
print(' '.join(r))
