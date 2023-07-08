import sys
from collections import defaultdict
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

#
# #
#

filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

seq = lines[0]

aa, ab = map(float, lines[5].split()[1:])
ba, bb = map(float, lines[6].split()[1:])

assert abs(aa+ab - 1.0) < 0.000001
assert abs(ba+bb - 1.0) < 0.000001 

t = {}
t['AA'] = aa
t['AB'] = ab
t['BA'] = ba
t['BB'] = bb

res = 1.00
for i in range(len(seq)-1):
    key = seq[i:i+2]
    res *= t[key]
print(res/2)
