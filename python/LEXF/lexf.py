import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


def addone(a, max):
    n = len(a)
    i = 0
    while True:
        if i == n:
            break
        #print(f'i {i} char {a[i]}')
        a[i] = a[i] + 1
        if a[i] < max:
            return a
        else:
            a[i] = 0
            i += 1



def atostr(a, ita):
    res = ''
    for i in a:
        assert isinstance(i, int)
        res += ita[i]
    return res
#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 2

alp = lines[0].split(' ')
n = int(lines[1])

ati = {}
ita = {}
for i in range(len(alp)):
    ati[alp[i]] = i
    ita[i] = alp[i]

print(alp)
print(ati)
print(ita)
print(n)

ntot = len(alp)**n
print(f'ntot {ntot}')
a = [0 for i in range(n)]
print(atostr(a, ita)[::-1])
for i in range(ntot - 1):
    a = addone(a,len(alp))
    print(atostr(a, ita)[::-1])
