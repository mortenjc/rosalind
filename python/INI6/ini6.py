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

assert len(lines) == 1

wset = set()
count = {}
words = lines[0].split(' ')
for w in words:
    if not w in wset:
        count[w] = 1
    else:
        count[w] += 1
    wset.add(w)

for i in count:
    print(i, count[i])
