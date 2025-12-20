import sys

sys.path.append('../common')
import toolbox as tb
import files as f
from functools import cache

# https://rosalind.info/problems/fibd

filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

assert len(lines) == 1

n, d = lines[0].split(' ')
n = int(n)
d = int(d)

print(n, d)



@cache
def f(n, r):
    if n==2 or n == 1:
        return 1

    if n <= r:
        return f(n-1,r) + f(n-2, r)

    else: 
        if n > r:
            return sum( f(n-i,r) for i in range(2, r + 1) )

for i in range(1, 7):
    print(i, f(i, 3))

print(f(99,16))
# 99, 16 => 215182717852492203481

print(f(n,d))