import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/long


def ovlmerge(s1, s2):
    assert len(s2) > len(s1)
    s1 += ' ' * (len(s2) - len(s1))
    res = ''
    for i in range(len(s2)):
        if s2[i] == ' ':
            res += s1[i]
        elif s1[i] == ' ':
            res += s2[i]
        else:
            if s2[i] != s1[i]:
                print(s1)
                print()
                print(s2)
                print(f's2[{i}] == {s2[i]} / s1[{i}] == {s1[i]}')
                assert 1 == 0, 'overlap mismatch'
            res += s2[i]
    return res


def splice(res, strings, start, end):
    next = start
    indent = 0
    final = strings[start]
    d = set()
    idx = 0
    while True:
        i = res[next]
        print(f'idx {idx:2} next {next:2}, i {i} at indent {indent}')

        d.add(next)
        s1 = final
        indent += i[1]
        s2 = f'{" "*(indent)}{strings[i[0]]}'
        final = ovlmerge(s1, s2)
        next = i[0]
        idx += 1
        if next == end:
            print('done')
            return final


def getstartnend(res):
    left = set()
    right = set()
    for i in res:
        print(f'{i} {res[i]}')
        left.add(i)
        right.add(res[i][0])

    start = list(left.difference(right))
    end = list(right.difference(left))

    print(f'len(res) {len(res)}')
    assert len(start) == 1
    assert len(end) == 1

    start = start[0]
    end = end[0]
    print(f'start {start}, end {end}')
    return start, end


def match(i, j, strings):
    ref = strings[i]
    cmp = strings[j]

    res = s.longest_overlap(ref, cmp)
    if res[1] < len(ref) // 2:
        return []
    else:
        print(
            f'match {i}, {j}, len(ref) {len(ref)}, len(cmp) {len(cmp)} len(ss) {res[1]}'
        )
        return [j, res[0]]


def inc(i, j, n):
    j += 1
    if j == n:
        i += 1
        j = 0
    return i, j


def findoverlaps(strings):
    n = len(strings)
    res = {}
    f = set()
    t = set()
    i = 0
    j = 0

    while True:
        if i == n:
            print('done')
            return res
        elif (i in f) or (j in t):  # skip already matched
            i, j = inc(i, j, n)
        elif i == j:  # ship self check
            i, j = inc(i, j, n)
        else:
            m = match(i, j, strings)
            if m == []:  # no match
                i, j = inc(i, j, n)
            else:  # match
                f.add(i)
                t.add(j)
                res[i] = m
                i += 1
                j = 0


#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, strings = f.readfasta(lines)

r = findoverlaps(strings)

start, end = getstartnend(r)

final = splice(r, strings, start, end)
print(f'---\n{final}\n---')
print(f'len(final) {len(final)}')
