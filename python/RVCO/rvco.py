import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import graphe

# https://rosalind.info/problems/rvco

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs = f.readfasta(lines)

res = 0
for seq in seqs:
    if tb.revcompl(seq) == seq:
        res += 1
        print(seq)

print(res)
