import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

def setmodm(n, m):
    res = 1
    for i in range(1, n+1):
        #print(i)
        res *= 2
        res = res % m
    return res

#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 1
n = int(lines[0])
print(n)
res = setmodm(n,1000000)
print(res)
