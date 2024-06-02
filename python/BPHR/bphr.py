import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/bphr


#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs, qual = f.readfastq(lines[1:])

q = int(lines[0])
print(f'threshold {q}')

lowq = 0
seqlen = len(seqs[0])
for j in range(seqlen):
    qavg = 0
    for i in range(n):
        qavg += ord(qual[i][j]) - ord('!')
    qavg = qavg / n
    if qavg < q:
        lowq += 1

print(lowq)
