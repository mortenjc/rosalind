import sys, queue, math
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)


def findreversals(lst):
    reversals = 0
    stack = []
    res = []
    first = lst[0]
    next = lst[1]
    if next > first:
        res.append(first)
        state = 1 #asc
    else:
        state = 2 #dec
        stack.append(first)

    for i in range(1, len(lst)-1):
        first = lst[i]
        next = lst[i+1]
        #print('first', first, 'next', next)
        if next > first:
            newstate = 1 #asc
        else:
            newstate = 2 #dec

        if state == 1:
            res.append(first)
        if state == 2:
            stack.append(first)

        if state == 1 and newstate == 2:
            stack.append(first)
            state = newstate
            continue
        if state == 2 and newstate == 1:
            if len(res) > 0:
                res.pop()
            reversals += 1
            print('reverse', stack)
            for _ in range(len(stack)):
                res.append(stack.pop())
            stack = []
            state = newstate
            continue

    if state == 2 and len(stack) != 0:
        stack.append(next)
        reversals += 1
        print('reverse', stack)
        for _ in range(len(stack)):
            res.append(stack.pop())

    if state == 1:
        res.append(next)

    return res, reversals


# reverse sublist starting from (including) begin
# and ending with (excluding) end
# def reverse(s, begin, end):
#     mid = s[begin:end]
#     return s[:begin] + mid[::-1] + s[end:]
#assert reverse([1,2,3,4,5], 1, 4) == [1, 4, 3, 2, 5]

def doit(nlist):
    res, rev = findreversals(nlist)
    print(f'{rev} reversal(s):')
    print(nlist)
    print(res)



doit([9, 8, 7, 6, 5, 4, 3, 2])
doit([2, 3, 4, 5, 6, 7, 8, 9])
doit([1, 2, 7, 4, 3, 19, 18, 20])
doit([3, 1, 5, 2, 7, 4, 9, 6, 10, 8])

#print(tp[:r[0]])
# for i in range(len(r)-1):
#     print(tp[r[i]:r[i+1]])

# https://rosalind.info/problems/rear

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs = f.readfasta(lines)
#print(n, names, strings)
