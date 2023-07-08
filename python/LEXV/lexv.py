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


def strtoint(a, ati):
    n = len(ati)
    res = 0
    arev = a[::-1]
    for i in range(len(a)):
        res += (n**i)*ati[arev[i]]
    return res

tmp = {'D':1, 'N':2, 'A':3 }
assert strtoint('D', tmp) == 1
assert strtoint('N', tmp) == 2
assert strtoint('A', tmp) == 3
assert strtoint('DD', tmp) == 4
assert strtoint('DN', tmp) == 5
assert strtoint('DA', tmp) == 6
assert strtoint('DDD', tmp) == 13


def gt(s, t, ati):
    #print(s,t)
    tp = t[:len(s)]
    if s == tp:
        return False
    else:
        i1 = strtoint(s, ati)
        i2 = strtoint(tp, ati)
        return i1 > i2

#assert gt('DD', 'D', tmp)
#assert not gt('DDD', 'DDD', tmp)

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
#n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

assert len(lines) == 2

alp = lines[0].split(' ')
n = int(lines[1])


# generate dictionaries
ati = {}
ita = {}
for i in range(len(alp)):
    ati[alp[i]] = i
    ita[i] = alp[i]

print(alp)
print(ati)
print(ita)
print(n)

orgstr = []
for l in range(1,n+1):
    #print(f'l {l}')
    ntot = len(alp)**l
    #print(f'ntot {ntot}')
    a = [0 for i in range(l)]
    tmp = atostr(a, ita)[::-1]
    #print(tmp)
    orgstr.append(tmp)
    for i in range(ntot - 1):
        a = addone(a,len(alp))
        tmp = atostr(a, ita)[::-1]
        #print(tmp)
        orgstr.append(tmp)

#print(orgstr)
n2 = len(orgstr)
#print(n2)

print('sorting... please wait (use pypy and wait a little shorter)')


for i in range(n2):
    for j in range(i,n2):
        s = orgstr[i]
        t = orgstr[j]
        if gt(s, t, ati):
            tmp = orgstr[i]
            orgstr[i] = orgstr[j]
            orgstr[j] = tmp

for i in orgstr:
    print(i)
