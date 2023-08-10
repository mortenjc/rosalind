import sys, queue, math
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import numpy as np

sys.setrecursionlimit(10000)

# https://rosalind.info/problems/mmch

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs = f.readfasta(lines)
#print(n, names, strings)

assert n == 1

res = tb.aminostat(seqs[0])
print(res)

# If AU and CG counts do not match we first need to
# do n choose k (max, max-min)

minau = min(res['A'],res['U'])
maxau = max(res['A'],res['U'])
chooseau = math.comb(maxau, maxau-minau)

mincg = min(res['C'],res['G'])
maxcg = max(res['C'],res['G'])
choosecg = math.comb(maxcg, maxcg-mincg)

print('AU:',minau, maxau, chooseau)
print('CG:',mincg, maxcg, choosecg)

# then there are k! possible pairs for each og AU and CG
print(chooseau*choosecg*math.factorial(minau)*math.factorial(mincg))
