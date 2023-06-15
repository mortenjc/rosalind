import sys
sys.path.append('../common')
import toolbox as tb

# https://rosalind.info/problems/orf

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'test.txt'

n, names, strings = tb.readfasta(filename)


def orf(sequence):
    res = set()
    for i in range(3):
        seq = sequence[i:]
        starts = tb.startcodons(seq)
        # if len(starts) == 0:
        #     continue
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
