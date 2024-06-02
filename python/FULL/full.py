import sys, queue, math

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)

mw = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}


def prtweight(seq):
    res = 0.0
    for p in seq:
        res += mw[p]
    return res


def bestmatch(w):
    best = 10000.0
    prt = ''
    for p in mw:
        diff = math.fabs(mw[p] - w)
        if diff < best:
            best = diff
            prt = p
    print(prt, best)
    return prt


# https://rosalind.info/problems/mmch

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs = f.readfasta(lines)
# print(n, names, strings)

total = float(lines[0])
weights = list(map(float, lines[1:]))
print(weights)

assert len(weights) % 2 == 0

protein = ''
for i in range(len(weights) // 2 - 1):
    print('test', weights[i + 1], weights[i])
    weight = weights[i + 1] - weights[i]
    print(weight)
    protein += bestmatch(weight)

print(protein)
print(prtweight(protein))
print(prtweight('KEKEP'))
