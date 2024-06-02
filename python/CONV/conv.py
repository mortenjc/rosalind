import sys, queue, math

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)


def round(n):
    return int(n * 10000) / 10000


md = {}
ms = set()


def add(s):
    if s in ms:
        md[s] += 1
    else:
        md[s] = 1
        ms.add(s)


# https://rosalind.info/problems/conv

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs = f.readfasta(lines)
# print(n, names, strings)

assert len(lines) == 2

l1 = list(map(float, lines[0].split()))
l2 = list(map(float, lines[1].split()))

for a in l1:
    for b in l2:
        diff = round(a - b)
        add(diff)


max_value = max(md, key=md.get)
print(md[max_value])
print(max_value)
