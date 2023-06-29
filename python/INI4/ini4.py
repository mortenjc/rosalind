import sys, math
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 1
a = int(lines[0].split()[0])
b = int(lines[0].split()[1])

res = 0
for i in range(a, b+1):
    if i & 0x1 == 1:
        res += i
print(res)
