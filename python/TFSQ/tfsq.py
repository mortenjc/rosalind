import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import stats as st

# https://rosalind.info/problems/tfsq


#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, name, seqs, qual = f.readfastq(lines)


for i in range(n):
    print('>' + name[i])
    seq = seqs[i]
    lseq = len(seq)

    w=70
    start = 0
    end = min(len(seq), w)
    while start < lseq:
        #print(start, end)
        assert len(seq[start:end]) <= w
        print(seq[start:end])
        start += w
        end += min(w, lseq - start)
