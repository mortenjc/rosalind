import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import graphe

# https://rosalind.info/problems/filt
def qval(c):
    return ord(c) - ord('!')


def average_qual(qual):
    sum = 0
    for i in range(len(qual)):
        sum += qval(qual[i])
    return sum//len(qual)

def count_below(qual, lim):
    count = 0
    for i in range(len(qual)):
        if qval(qual[i]) < lim:
            count += 1
    return count

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs, qual = f.readfastq(lines[1:])

q = int(lines[0])
print(q)

res = 0
for i, qstr in enumerate(qual):
    avg = average_qual(qstr)
    print(i, avg, count_below(qstr, ))
print(res)
