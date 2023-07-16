import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

sys.setrecursionlimit(10000)

# https://rosalind.info/problems/edit


#
# #
#


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs = f.readfasta(lines)
#print(n, names, strings)

assert n == 2

s1 = seqs[0]
m = len(s1)
s2 = seqs[1]
n=len(s2)
print(f's1 len: {len(s1)}')
print(f's2 len: {len(s2)}')
c, l = s.lcs_length(s1,s2)
print('len:', l)
lcs = s.lcs_backtrack(c, s1, s2, m, n)

print(f'delete {m-l} from s1 to get')
print(lcs)
print(f'add {n-l} to lcs get s2')

print(max(n-l, m-l))
