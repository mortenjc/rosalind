import sys, re

sys.path.append('../common')
import toolbox as tb


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'test.txt'

f = open(filename, "r")
data = f.read()
lines = data.splitlines()
f.close()

print(len(lines))

res = tb.codonmult['*']
for i in lines[0]:
    res *= tb.codonmult[i]
    if res > 1000000:
        res = res % 1000000

print(res)
