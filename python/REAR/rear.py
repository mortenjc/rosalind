import sys, queue, math
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



# https://rosalind.info/problems/rear

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs = f.readfasta(lines)
#print(n, names, strings)
