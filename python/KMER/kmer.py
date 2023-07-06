import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import stats as st

# https://rosalind.info/problems/afrq

def itoa(i, k, l):
    res = ''
    rem = i
    for j in range(k-1,-1,-1):
        #print(j, k**j)
        c = rem//(k**j)
        res += l[c]
        #print(j, rem, c, l[c])
        rem = rem - c*(k**j)
    return res


#
# #
#

filename = f.filefromargv(sys.argv)
n, names, seqs = f.readfasta(filename)
lines = f.readlines(filename)

assert n == 1

l = {0:'A', 1:'C', 2:'G', 3:'T'}
#l = {'A':0, 'C':1, 'G':2, 'T':3}
k = 4

nmax = 4**4

pat = []
for i in range(256):
    pat.append(itoa(i, 4, l))


res = []
for p in pat:
    f = s.findall(seqs[0], p)
    res.append(str(len(f)))

print(' '.join(res))
