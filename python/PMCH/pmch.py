import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import intlists as il

# https://rosalind.info/problems/pmch

filename = f.filefromargv(sys.argv)
n, names, strings = f.readfasta(filename)
#lines = f.readlines(filename)

assert n == 1
r = tb.aminostat(strings[0])

assert r['A'] == r['U']
assert r['C'] == r['G']

res = math.factorial(r['A'])*math.factorial(r['C'])
print(res)
