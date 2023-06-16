import sys
sys.path.append('../common')
import toolbox as tb
import files as f

# https://rosalind.info/problems/orf

filename = f.filefromargv(sys.argv)
n, names, strings = f.readfasta(filename)


def orf(sequence):
    res = set()
    for i in range(3):
        seq = sequence[i:]
        starts = tb.startcodons(seq)
        for j in starts:
            tmp = tb.openframe(seq[j:])
            if tmp != '':
                res.add(tmp)
    return res

orgsequence = strings[0]
res = orf(orgsequence)

# REVERSE COMPLEMENT
revsequence = tb.revcompl(orgsequence)
res = res | orf(revsequence)
for i in res:
    print(i)
