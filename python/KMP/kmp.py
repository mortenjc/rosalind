import sys
from pathlib import Path
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s

A = {'A': 0, 'G' : 1, 'C': 2, 'T':3}

def KMP(pat):
    R = 4
    M = len(pat)
    dfa = [[0 for i in range(M)] for j in range(R)]
    dfa[A[pat[0]]][0] = 1
    X = 0
    for j in range(1, M):
        for c in range(R):
            dfa[c][j] = dfa[c][X]
        dfa[A[pat[j]]][j] = j + 1
        X = dfa[A[pat[j]]][X]
    return dfa


def KMP_search(s1, pat):
    M = len(pat)
    dfa = KMP(pat)
    # for r in dfa:
    #     print(r)
    j = 0
    for i in range(len(s1)):
        if j >= M:
            break
        j = dfa[A[s1[i]]][j]
    if j == M:
        return i - M, j
    else:
        return -1, j

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, seqs = f.readfasta(lines)
#all = Path(filename).read_text()

s = seqs[0]
ls = len(s)
print('len:', ls)
p = [0] * ls



if False:
    for k in range(1,ls):
        if k % 1000 == 0:
            print(k)
        for j in range(1,k):
            subs = s[j:k]

            if s.find(subs) == 0:
                print(j, k, s)
                print(j,k, subs)
                p[k] = len(subs)
                break

    print(p)
    print('-------')



def kmp_failure(s):
    l = len(s)
    i = 1
    j = 0
    f = [0] * l
    while i < l:
        if s[j] == s[i]:
            f[i] = j + 1
            i += 1
            j += 1
        elif j != 0:
            j = f[j - 1]
        else:
            f[i] = 0
            i += 1
    return f


res = kmp_failure(s)

print(' '.join(map(str, res)))
