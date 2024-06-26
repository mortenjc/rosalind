import sys

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)

# https://rosalind.info/problems/glob


# Levenstein distance adapted to pythonm from
# https://en.wikipedia.org/wiki/Levenshtein_distance
def mineditlen(s, t):
    gp = 5  # gap penalty
    m = len(s)
    n = len(t)
    C = np.ndarray((m + 1, n + 1))
    for i in range(m + 1):
        C[i, 0] = i * gp
    for j in range(n + 1):
        C[0, j] = j * gp

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            substcost = -tb.blosum62[s[i - 1] + t[j - 1]]
            minval = min(
                C[i - 1, j] + gp, C[i, j - 1] + gp, C[i - 1, j - 1] + substcost
            )
            # print(f'({i},{j}) {s[i-1]}, {t[j-1]}: {substcost} (min {minval})')
            C[i, j] = minval

    return C, C[m, n]


def backtrack(C, s, t):
    i = len(s)
    j = len(t)
    s2 = ''
    t2 = ''
    matches = 0
    while i != 0 or j != 0:
        minval = min(C[i - 1, j - 1], C[i - 1, j], C[i, j - 1])
        if minval == C[i - 1, j - 1]:  # subst or match
            if s[i - 1] == t[j - 1]:
                matches += 1
            s2 = s[i - 1] + s2
            t2 = t[j - 1] + t2
            i -= 1
            j -= 1
        elif minval == C[i - 1, j]:  # ins?
            s2 = s[i - 1] + s2
            t2 = '-' + t2
            i -= 1
        else:
            s2 = '-' + s2
            t2 = t[j - 1] + t2
            j -= 1

    return s2, t2, matches


#
# #
#


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs = f.readfasta(lines)
# print(n, names, strings)

assert n == 2

s1 = seqs[0]
m = len(s1)
s2 = seqs[1]
n = len(s2)
print(f's1 len: {len(s1)}')
print(f's2 len: {len(s2)}')
c, l = mineditlen(s1, s2)
print('len:', l)
# print(c)
s2, t2, m = backtrack(c, s1, s2)
assert len(s2) == len(t2)
print()
print(len(s2) - m)
print(s2)
print(t2)
