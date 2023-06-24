import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/long


def ovlmerge(s1,s2):
    assert len(s2) > len(s1)
    s1 += ' '*(len(s2) - len(s1))
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
        #print(s1)
        #print(s2)
        #print(final)
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


def subsn(n, cand):
    ss = []
    for i in range(len(cand),n, -1):
        ss.append(cand[:i])
    return ss


def match(i, j, strings, substrs):
    ref = strings[i]
    cmp = strings[j]
    #print(f'compare {i} to {j}')
    #print(substrs)
    for ss in substrs[j]:
        mat = s.findall(ref, ss)
        if mat != []:
            print(f'match {i}, {j}, len(ref) {len(ref)}, len(cmp) {len(cmp)} len(ss) {len(ss)}')
            print(mat)
            print(ref)
            print(f'{" "*(mat[0]-1)}{cmp}')

            #assert 1 == 0, 'debug'
            return [j, mat[0]-1]
    return []


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

    #create this table once
    substrns = []
    for tmpi in range(n):
        sn = len(strings[tmpi])//2
        substrns.append(subsn(sn, strings[tmpi]))

    while True:
        if i == n:
            print('done')
            return res
        elif (i in f) or (j in t): # skip already matched
            i, j = inc(i, j, n)
        elif i == j: # ship self check
            i, j = inc(i, j, n)
        else:
            m = match(i, j, strings, substrns)
            if m == []: # no match
                i, j = inc(i, j, n)
            else: # match
                f.add(i)
                t.add(j)
                res[i] = m
                i += 1
                j = 0


#
# #
#

filename = f.filefromargv(sys.argv)
n, names, strings = f.readfasta(filename)
#lines = f.readlines(filename)¨

# for i in [15, 40, 26]:
#     print(names[i])
#     print(strings[i])
# sys.exit()

r = findoverlaps(strings)
# rosalind 4
#r = {0: [34, 464], 1: [18, 254], 2: [20, 264], 3: [2, 324], 4: [31, 430], 5: [33, 283], 6: [27, 385], 7: [14, 258], 8: [23, 458], 9: [13, 318], 10: [11, 267], 11: [42, 396], 12: [28, 479], 13: [30, 479], 14: [9, 384], 15: [40, 350], 16: [29, 425], 17: [38, 268], 18: [44, 274], 19: [0, 397], 20: [4, 354], 21: [47, 400], 22: [36, 414], 23: [12, 339], 24: [3, 346], 25: [19, 273], 26: [32, 465], 27: [21, 469], 28: [10, 370], 29: [24, 387], 30: [45, 272], 31: [39, 425], 32: [5, 307], 33: [22, 432], 34: [6, 321], 35: [48, 295], 36: [8, 284], 37: [46, 447], 38: [43, 377], 39: [37, 418], 40: [26, 387], 41: [1, 288], 42: [17, 314], 43: [49, 276], 45: [41, 343], 46: [7, 306], 47: [16, 385], 48: [25, 265], 49: [35, 441]}
print(r)

start, end = getstartnend(r)

final = splice(r, strings, start, end)
print(f'<<{final}>>')
print(f'len(final) {len(final)}')
