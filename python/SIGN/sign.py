import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

def permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = [lst[i]]
        remlst = lst[:i] + lst[i+1:]
        for p in permutations(remlst):
            l.append(m + p)
    return l


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

n = int(lines[0])

assert n <= 6

l = list(range(1,n+1))
usperm = permutations(l)
#print(usperm)
signs = []
for i in range(2**n):
    a = '{:08b}'.format(i)
    a2 = a[-n:]
    b = list(map(int,list(a2)))
    for i in range(len(b)):
        if b[i] == 0:
            b[i] = 1
        else:
            b[i] = -1
    signs.append(b)

result = []
for l1 in usperm:
    for l2 in signs:
        #print(f'{l1} {l2}')
        res = []
        for i1, i2 in zip(l1, l2):
            res.append(i1 * i2)
        result.append(res)

print(len(result))
for i in result:
    print(' '.join(list(map(str,i))))
