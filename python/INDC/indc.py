import sys, math

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import stats as st

#
# #
#


filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
# print(n, names, strings)
lines = f.readlines(filename)

n = int(lines[0].split()[0])
print(n)

p = 0.5
r = []
for i in range(1, 2 * n + 1):
    res = 0.0
    for j in range(i, 2 * n + 1):
        res += st.bern(2 * n, j, p)
    r.append(f'{math.log10(res):.3f}')
    print(f'{i} {res:.3f} {math.log10(res):.4f}')

print(' '.join(r))
