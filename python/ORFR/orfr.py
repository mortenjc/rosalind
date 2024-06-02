import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/rvco

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs = f.readfasta(lines)

assert len(lines) == 1

seq = lines[0]
rseq = tb.revcompl(seq)


def findlongest(seq):
    result = ''
    res = s.findall(seq, 'ATG')
    for offset in res:
        a = ''
        for i in range(offset - 1, len(seq) - offset, 3):
            nseq = seq[i : i + 3]
            am = tb.amino(nseq)
            # print(i, nseq, am)
            if am == '*':
                break
            a += tb.amino(nseq)
        if len(a) > len(result):
            result = a
    return result


res = []
res.append(findlongest(seq))
res.append(findlongest(rseq))
print(max(res))
