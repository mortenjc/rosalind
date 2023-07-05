import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/rstr

def bern(n, k, p):
    assert p <= 1.0
    q = 1.0 - p
    return math.comb(n,k)* p**k * q**(n-k)

#
# #
#

filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 2

N = int(lines[0].split()[0])
GC = float(lines[0].split()[1])
AT = 1.0 - GC

seq = lines[1]
print(seq)
print(N, GC)

stat = tb.aminostat(seq)
cat = stat['A'] + stat['T']
cgc = stat['G'] + stat['C']
assert cat + cgc == len(seq)
print(f'cat {cat}, cgc {cgc}')

res = []

newp = (GC/2)**cgc * (AT/2)**cat
lg10newp = cgc * math.log10(GC/2) + cat * math.log10(AT/2)
res.append(int(lg10newp*1000)/1000.0)
print(newp)
print(' '.join(map(str, res)))


p = newp
res = 0.0
for i in range(1, 50):
    res += bern(N,i,p)

print(res)
