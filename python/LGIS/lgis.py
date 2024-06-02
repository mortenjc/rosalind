import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import intlists as il

# https://rosalind.info/problems/lgis

filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

n = int(lines[0])
seq = []
for l in lines[1:]:
    ll = l.split(' ')
    seq += ll

assert n == len(seq)

# increasing
res = il.long_sseq(il.listofint(seq))
print(' '.join(il.listofstr(res)))

# decreasing
res = il.long_sseq(il.listofint(seq), False)
print(' '.join(il.listofstr(res)))
