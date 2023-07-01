import sys
from collections import defaultdict
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


def maj(line, n):
    lst = list(map(int, line.split()))
    assert len(lst) == n
    count = defaultdict(int)
    for i in lst:
        count[i] += 1
        if count[i] > n//2:
            return i
    return -1



#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

k, n = list(map(int,lines[0].split()))

assert len(lines) == k + 1

res = []
for line in lines[1:]:
    res.append(str(maj(line, n)))

print(' '.join(res))
