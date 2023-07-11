import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import graphe

# https://rosalind.info/problems/filt

def qval(c):
    return ord(c) - ord('!')

def quality_count(qstr, val):
    c = 0
    for i in range(len(qstr)):
        if qval(qstr[i]) >= val:
            c+=1
    #print(c, len(qstr), c*100//len(qstr))
    return c*100//len(qstr)

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs, qual = f.readfastq(lines[1:])

q,p = list(map(int, lines[0].split()))
print(q,p)

res = 0
for qstr in qual:
    qc = quality_count(qstr,q)
    print(qc,p)
    if qc >= p:
        res += 1
print(res)
