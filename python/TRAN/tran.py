import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


filename = f.filefromargv(sys.argv)
n, names, strings = f.readfasta(filename)
#print(n, names, strings)

assert n == 2

s1 = strings[0]
s2 = strings[1]

def is_transition(c1, c2):
    ts = {'A': 'G', 'G':'A', 'C':'T', 'T':'C'}
    return c1 == ts[c2]

def is_transversion(c1, c2):
    if c1 == 'A' and (c2 == 'T' or c2 == 'C'):
        return True
    if c1 == 'C' and (c2 == 'A' or c2 == 'G'):
        return True
    if c1 == 'T' and (c2 == 'A' or c2 == 'G'):
        return True
    if c1 == 'G' and (c2 == 'T' or c2 == 'C'):
        return True
    return False

assert is_transition('A', 'G')
assert not is_transition('A', 'T')


transi = 0
transv = 0
for i in range(len(s1)):
    c1 = s1[i]
    c2 = s2[i]
    #print(f'i {i}, c1 {c1}, c2 {c2}')
    if c1 != c2:
        if is_transition(c1, c2):
            transi += 1
            continue
        if is_transversion(c1, c2):
            transv += 1
            continue

print(f'ratio {transi*1.0/transv}')
