import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import stats as st

# https://rosalind.info/problems/phre

def avgqual(s):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i]) - ord('!')
    return sum/len(s)

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, name, seqs, qual = f.readfastq(lines[1:])

val = int(lines[0])

count = 0
for i in range(n):
    if avgqual(qual[i]) < val:
        count += 1

print(count)
