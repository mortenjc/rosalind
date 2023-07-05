import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

# https://rosalind.info/problems/cat

cmpl = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}

def is_compl(A, B):
    return cmpl[A] == B

def check(substr):
    a = [substr.count(nuc) for nuc in 'AUGC']
    return a[0] == a[1] and a[2] == a[3]

bondings = {}


def nonx_perf_bond(seq):
    if len(seq) != 0:
        print(seq)
    if len(seq) <= 2:
        return 1
    elif seq in bondings:
        print(f'{seq} : {bondings[seq]}')
        return bondings[seq]

    splits = [i for i in range(1, len(seq), 2) if is_compl(seq[0], seq[i]) and check(seq[1:i])]
    print(f'splits: {splits}')
    tmp = sum([nonx_perf_bond(seq[1:i])*nonx_perf_bond(seq[i+1:]) for i in splits]) % 1000000
    print(f'{seq} -> {tmp}')
    bondings[seq] = tmp

    return bondings[seq]



#
# #
#

filename = f.filefromargv(sys.argv)
n, names, strings = f.readfasta(filename)
#lines = f.readlines(filename)
assert n == 1
print(strings[0])
l = len(strings[0])

print('len', l)
seq = strings[0]

r = nonx_perf_bond(seq)
print(r)
