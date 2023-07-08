import sys, math
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#

filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

V, E = map(int, lines[0].split(' '))
print(f'vertices {V}, edges {E}')

u = set()
deg = {}

for line in lines[1:]:
    a, b = map(int, line.split(' '))
    if not a in u:
        deg[a] = [b]
    else:
        deg[a].append(b)
    if not b in u:
        deg[b] = [a]
    else:
        deg[b].append(a)
    u.add(a)
    u.add(b)

print(deg)
print()

res = dict(sorted(deg.items()))
r = []
for i in range(1,V+1):
    if not i in u:
        r.append(str(0))
        continue
    sum = 0
    for j in res[i]:
        sum += len(res[j])
    r.append(str(sum))

print(' '.join(r))
