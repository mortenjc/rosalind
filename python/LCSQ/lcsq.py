import sys

sys.path.append('../common')
import toolbox as tb
import numpy as np
import files as f
import strings as s

sys.setrecursionlimit(10000)

# https://rosalind.info/problems/lcsq


# Adapted to python from
# https://en.wikipedia.org/wiki/Longest_common_subsequence
def LCSLength(X, Y):
    print(X)
    print()
    print(Y)
    m = len(X)
    n = len(Y)
    C = np.ndarray((m + 1, n + 1))
    for i in range(m + 1):
        C[i, 0] = 0
    for j in range(n + 1):
        C[0, j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                C[i, j] = C[i - 1, j - 1] + 1
            else:
                C[i, j] = max(C[i, j - 1], C[i - 1, j])
    return C, int(C[m, n])


def backtrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    if X[i - 1] == Y[j - 1]:
        return backtrack(C, X, Y, i - 1, j - 1) + X[i - 1]
    if C[i, j - 1] > C[i - 1, j]:
        return backtrack(C, X, Y, i, j - 1)
    return backtrack(C, X, Y, i - 1, j)


# My own invention
def issubseq(s, seq):
    i = 0
    j = 0
    while i < len(seq):
        if i == len(seq) or j == len(s):
            break
        if seq[i] == s[j]:
            i += 1
            j += 1
        else:
            j += 1

    if i == len(seq):
        return True
    else:
        return False


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
c, l = LCSLength(s1, s2)
print('len:', l)
print(backtrack(c, s1, s2, m, n))

assert issubseq('ATCGATCG', 'A')
assert issubseq('ATCGATCG', 'ACG')
assert issubseq('ATCGATCG', 'ATAT')
assert issubseq('ATCGATCG', 'AGTG')
