import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/prob


def point_mutation(seq1, seq2):
    assert len(seq1) == len(seq2)
    diffs = 0
    index = -1
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            #print(f'diff at {i}')
            diffs += 1
            index = i
    if diffs == 1:
        return index
    else:
        return -1

assert point_mutation('ATA', 'TTA') == 0
assert point_mutation('ATA', 'TAT') == -1


#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, strings = f.readfasta(lines)


good = []
seen = set()
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        if (i in seen) or (j in seen):
            continue
        if strings[i] == strings[j]:
            good.append(strings[i])
            seen.add(i)
            seen.add(j)
            continue
        if strings[i] == tb.revcompl(strings[j]):
            good.append(strings[i])
            good.append(strings[j])
            seen.add(i)
            seen.add(j)

print(good)

bad = []
for i in range(n):
    if not strings[i] in good:
        bad.append(strings[i])

print(bad)

for b in bad:
    for g in good:
        #print(f'test if {b} matches {g} or {tb.revcompl(g)}')
        pmidx = point_mutation(g,b)
        if  pmidx != -1:
            print(f'{b}->{g}')
            break
        pmidx = point_mutation(tb.revcompl(g),b)
        if  pmidx != -1:
            print(f'{b}->{tb.revcompl(g)}')
            break
