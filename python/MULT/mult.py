import sys, queue

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)

# https://rosalind.info/problems/mult


#
# #
#


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs = f.readfasta(lines)
# print(n, names, strings)


tb.global_alignment(seqs[1], seqs[2], (0, 1, 1))
