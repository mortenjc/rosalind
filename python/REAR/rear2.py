import sys, queue, math, random

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)


# reverse sublist starting from (including) begin
# and ending with (excluding) end
def reverse(s, begin, end):
    mid = s[begin:end]
    return s[:begin] + mid[::-1] + s[end:]
assert reverse([1,2,3,4,5], 1, 4) == [1, 4, 3, 2, 5]


def score(s1, s2):
    assert len(s1) == len(s2)
    score = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            score += 1
    return score

assert score([1,2,3], [3,2,1]) == 1
assert score([1,2,3], [1,2,3]) == 3

s1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s2 = [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]


def matches(s1, s2):
    assert len(s2) == len(s1)
    ob = 0
    oe = len(s2) - 1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            break
        ob += 1
    for i in range(len(s1)-1, 0, -1):
        if s1[i] != s2[i]:
            break
        oe-= 1
    return ob, oe

# res = matches([1, 2, 3, 4, 5, 6, 7], [1, 2, 5, 3, 4, 6, 7])
# assert res == (2,4), print(res)
# res = matches([1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7])
# assert res == (2,4), print(res)



oe = 9
ob = 0
q = deque()
seen = set()
q.append((0, s2))

while True:
    n, b, e, s = popleft(q)
    if (n, s) in seen:
        continue

    if n == 1:
        ob = 0
        oe = 9
        s = s2
    b = random.randint(ob, oe-1) # inclusive
    e = random.randint(b+1, oe) # inclusice

    # state = (tuple(s), n, b, e)
    # if state in seen:
    #     print('duplicate')
    #     continue
    # seen.add(state)
    # #print(f'new state: {} {} {}')

    tmp = reverse(s, b, e+1)
    print(f'reverse {b}, {e}: {s} -> {tmp} ')
    ob, oe = matches(s1, tmp)
    if oe <= ob:
        print(f'candidate {n}')
        n= 1
        break

    s = tmp

    n += 1
    if n > 10:
        print('---------- restart')
        n = 1




# https://rosalind.info/problems/rear

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
# n, names, seqs = f.readfasta(lines)
# print(n, names, strings)
