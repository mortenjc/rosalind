import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/ba1a

#
# #
#

def match(s1, pat):
    count = 0
    ls1 = len(s1)
    l = len(pat)
    assert ls1 >= l

    for i in range(ls1 - l + 1):
        if s1[i:i+l] == pat:
            count += 1
    return count


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs, qual = f.readfastq(lines[1:])

seq = lines[0]

print(tb.revcompl(seq))
