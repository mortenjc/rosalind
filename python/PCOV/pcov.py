import sys, queue
from pathlib import Path
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import stats


def makepair(s1):
    a = s1[:-1]
    b = s1[1:]
    assert len(a) == len(b)
    return (a, b)

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, strings = f.readfasta(lines)
#all = Path(filename).read_text()

res = set()
for l in lines:
    revl = tb.revcompl(l)
    res.add(makepair(l))
    res.add(makepair(revl))

loop = {}
for a,b in res:
    loop[a] = b

start = lines[0][1:]
next = start
i = 0
s1 = start[0]
print(start)
while True:
    next = loop[next]
    s1 += next[0]
    if next == start:
        s1 = s1[:-1]
        break
    #print(f'{" "*(i+1)}{next}')
    i += 1
print()
print(s1)
