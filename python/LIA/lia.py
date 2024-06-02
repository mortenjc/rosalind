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

a = int(lines[0].split()[0])
b = int(lines[0].split()[1])
print(a, b)

n = 2**a
k = b
res = st.berni(n, k, 0.25)
print(f'{res:3.3}')
