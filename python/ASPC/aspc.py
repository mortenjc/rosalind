import sys, math

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


def facmodm(n, m):
    res = 1
    for i in range(1, n + 1):
        print(i, res)
        res *= i
    return res


def nchkmodm(n, k, m):
    print(n, k, m)
    res = facmodm(n, m) / (facmodm(k, m) * facmodm(n - k, m))
    print(res)
    return res


#
# #
#


filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

assert len(lines) == 1
n = int(lines[0].split()[0])
m = int(lines[0].split()[1])
print(n, m)

res = 0
for k in range(m, n + 1):
    # res += nchkmodm(n, k, 1000000)
    res += math.comb(n, k) % 1000000
print(int(res) % 1000000)
