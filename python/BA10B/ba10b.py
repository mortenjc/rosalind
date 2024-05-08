import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


# https://rosalind.info/problems/ba10b

#
# #
#




filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs, qual = f.readfastq(lines[1:])

s1 = lines[0]
alp = lines[2].split()

s2 = lines[4]
sts = lines[6].split()
mtx = lines[9:]

mtx = [x.split()[1:] for x in lines[9:]]

assert len(s1) == len(s2)

Dalp = {}
for i, l in enumerate(alp):
    Dalp[l] = i
Dsts = {}
for i, l in enumerate(sts):
    Dsts[l] = i

p = 1.0
for i in range(len(s1)):
    #print(f'{s1[i]} in state {s2[i]}')
    s = Dsts[s2[i]]
    v = Dalp[s1[i]]
    #print(f'{v} {s}')
    p = p * float(mtx[s][v])


#print(mtx)
print(f'{p:.12}')
