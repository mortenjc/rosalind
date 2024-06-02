import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


# https://rosalind.info/problems/2sum

#
# #
#


# Assumes sorted data
def find2sum(line):
    res = []
    b = 0
    e = len(line) - 1
    while True:
        bi = line[b]
        ei = line[e]
        if b >= e:
            break

        if (-bi) == ei:
            res.append([b, e, bi])
            b += 1
            e -= 1
            if bi != 0:
                break
        elif (-bi) < ei:
            e -= 1
        else:
            b += 1

    if len(res) == 0:
        return -1
    else:
        return res


assert find2sum([1, 2, 3]) == -1
assert find2sum([-3, 0, 3]) == [[0, 2, -3]]


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs, qual = f.readfastq(lines[1:])

n, k = map(int, lines[0].split())
assert n + 1 == len(lines)

for line in lines[1:]:
    D = {}
    res = -1
    linei = list(map(int, line.split()))
    for i in range(len(linei)):
        v = linei[i]
        if (-v) in D:
            res = (D[(-v)], i)
            break
        D[v] = i
    if res != -1:
        print(res[0] + 1, res[1] + 1)
    else:
        print(res)
