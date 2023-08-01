import sys, queue
from pathlib import Path
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import stats



def gc2prob(gc):
    pa = (1-gc)/2
    pg = gc/2
    return {'A':pa, 'T':pa, 'C':pg, 'G':pg}

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, strings = f.readfasta(lines)
#all = Path(filename).read_text()

N = int(lines[0])
s1 = lines[1]
sl = len(s1)
GC = list(map(float,list(lines[2].split(' '))))

print(N)
print(s1, sl)
print(GC)

substrs = N - sl + 1
print('substrings', substrs)

res = []
for i in range(len(GC)):
    p = gc2prob(GC[i])
    prob = 1.0
    for c in s1:
        prob *= p[c]
    res.append(prob*substrs)

print(' '.join(list(map(str,res))))
