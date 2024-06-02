import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/prob


#
# #
#

filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

seq = lines[0]
print(seq)
stat = tb.aminostat(seq)
cat = stat['A'] + stat['T']
cgc = stat['G'] + stat['C']
assert cat + cgc == len(seq)
print(f'cat {cat}, cgc {cgc}')

probs = list(map(float, lines[1].split(' ')))
print(probs)

res = []
for pgc in probs:
    pat = 1.0 - pgc
    # print(f'pgc {pgc}, pat {pat}')
    lg10newp = cgc * math.log10(pgc / 2) + cat * math.log10(pat / 2)
    res.append(int(lg10newp * 1000) / 1000.0)

print(' '.join(map(str, res)))
