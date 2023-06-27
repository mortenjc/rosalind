import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

def dist(s1, s2):
    assert len(s1) == len(s2)
    n = len(s1)
    diff = 0
    for i in range(n):
        if s1[i] != s2[i]:
            diff += 1
    return 1.0*diff/n

assert abs(dist('AB', 'AC') - 0.5) < 0.0001
assert abs(dist('ABC', 'ACC') - 0.3333) < 0.0001

#
# #
#


filename = f.filefromargv(sys.argv)
n, names, strings = f.readfasta(filename)
#lines = f.readlines(filename)
for i in range(n):
    dists = []
    for j in range(n):
        s1 = strings[i]
        s2 = strings[j]
        dists.append(str(f'{dist(s1, s2):.5f}'))
    print(' '.join(dists))
