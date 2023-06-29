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
assert a < 1000
assert b < 1000

print(a, b)
print(a**2 + b**2)
