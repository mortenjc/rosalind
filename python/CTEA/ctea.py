import sys, queue

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)

# https://rosalind.info/problems/ctea


# Levenstein distance adapted to python from
# https://en.wikipedia.org/wiki/Levenshtein_distance
def mineditlen(s, t):
    m = len(s)
    n = len(t)
    C = np.ndarray((m + 1, n + 1))
    for i in range(m + 1):
        C[i, 0] = int(i)
    for j in range(n + 1):
        C[0, j] = int(j)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                substcost = 0
            else:
                substcost = 1
            C[i, j] = int(
                min(C[i - 1, j] + 1, C[i, j - 1] + 1, C[i - 1, j - 1] + substcost)
            )

    return C, C[m, n]


def backtrack(C, s, t):
    i = len(s)
    j = len(t)
    s2 = ''
    t2 = ''
    while i != 0 or j != 0:
        minval = min(C[i - 1, j - 1], C[i - 1, j], C[i, j - 1])
        if minval == C[i - 1, j - 1]:  # subst or match
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

    return s2, t2


def backtrack2(C, s, t):
    q = queue.Queue()
    seen = set()
    q.put((C, s, t, ''))
    n = 1

    while not q.empty():
        C, s, t, p = q.get()
        i = len(s)
        j = len(t)
        # if (C, s, t) in seen:
        #     continue
        seen.add((C, s, t))
        print(f'({i},{j}) {s} {t}')
        print(p)
        print(C)

        if i == 0 or j == 0:
            print(n, n % 134217727)
            return

        diag = C[i - 1, j - 1]
        up = C[i - 1, j]
        left = C[i, j - 1]
        minval = min(diag, left, up)

        # At least two are equal
        count = -1
        dir = ''
        if minval == diag:
            dir += 'diag '
            q.put((C[0:i, 0:j], s[: i - 1], t[: j - 1], f'{p} ({i}, {j})'))
            count += 1
        if minval == up:
            dir += 'up '
            q.put((C[0:i, 0 : j + 1], s[: i - 1], t[:j], f'{p} ({i}, {j})'))
            count += 1
        if minval == left:
            dir += 'left '
            q.put((C[0 : i + 1, 0:j], s[:i], t[: j - 1], f'{p} ({i}, {j})'))
            count += 1

        if count > 0:
            dir = 'branch ' + dir

        print(dir)

        n *= 2**count
        continue


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

backtrack2(c, s1, s2)
