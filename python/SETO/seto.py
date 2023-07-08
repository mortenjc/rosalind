import sys
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

assert len(lines) == 3
n = int(lines[0])
a = set(map(int, lines[1][1:-1].split(',')))
b = set(map(int, lines[2][1:-1].split(',')))

#print(n)
U = set(range(1,n+1))
# print(U)
# print(a)
# print(b)
# print()

print(a | b)
print(a & b)
print(a - b)
print(b - a)
print(U - a)
print(U - b)
