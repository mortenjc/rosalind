import sys, math, re

sys.path.append('../common')
import toolbox as tb
import files as f

# https://rosalind.info/problems/sseq


def search(patt, string):
    res = patt.match(string)
    if res:
        return True
    return False


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, strings = f.readfasta(lines)

assert n == 2

string = strings[0]
patt = strings[1]
np = len(patt)
a = [f'({i})' for i in list(patt)]
repatt = '.*'.join(a)
print(string)
print(repatt)

pattern = re.compile(repatt)
for i in range(len(string)):
    # print(i)
    res = pattern.match(string[i:])
    if res:
        r = map(str, [1 + i + res.start(n) for n in range(1, np + 1)])
        print(r)
        print(' '.join(r))
        break
