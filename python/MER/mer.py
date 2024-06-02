import sys

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#


filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
# print(n, names, strings)
lines = f.readlines(filename)

assert len(lines) == 4

n = lines[0]
a1 = list(map(int, lines[1].split(' ')))
m = lines[2]
a2 = list(map(int, lines[3].split(' ')))

print(n, a1)
print(m, a2)

i = 0
j = 0
n = 0
res = []
while True:
    if i == len(a1):
        res.append(str(a2[j]))
        j = +1
    elif j == len(a2):
        res.append(str(a1[i]))
        i = +1
    # print(i,j, a1[i], a2[j])
    elif a1[i] <= a2[j]:
        print(a1[i])
        res.append(str(a1[i]))
        i += 1
    else:
        print(a2[j])
        res.append(str(a2[j]))
        j += 1
    n += 1
    if n == len(a1) + len(a2):
        break

print()
print(' '.join(res))
