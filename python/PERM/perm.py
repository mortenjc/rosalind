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
        m = lst[i]
        remlst = lst[:i] + lst[i+1:]

        for p in permutations(remlst):
            l.append(m + p)
    return l

assert permutations('') == []
assert permutations('A') == ['A']
assert permutations('AB') == ['AB', 'BA']

filename = f.filefromargv(sys.argv)
n, names, strings = f.readfasta(filename)
#print(n, names, strings)

val = int(strings[0])
strlst = [str(i + 1) for i in range(val)]
str = ''.join(strlst)
res = permutations(str)
print(len(res))
for i in res:
    print(' '.join(i))
