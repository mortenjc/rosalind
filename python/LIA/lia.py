import sys, math
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

def bern(n, k, p):
    assert p <= 1.0
    q = 1.0 - p
    return math.comb(n,k)* p**k * q**(n-k)

#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
#print(n, names, strings)
lines = f.readlines(filename)

a = int(lines[0].split()[0])
b = int(lines[0].split()[1])
print(a,b)

res = 0.0
n = 2**a
k = b
for i in range(k, n+1):
    res +=bern(n,i, 0.25)
print(f'{res:3.3}')
