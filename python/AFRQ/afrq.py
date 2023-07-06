import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import stats as st

# https://rosalind.info/problems/afrq


#
# #
#

filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 1

vals = s.tofloat(lines[0])

print(vals)

res = []
for p in vals:
    res.append(f'{st.berni(2,1,math.sqrt(p)):.3f}')
print(' '.join(res))
