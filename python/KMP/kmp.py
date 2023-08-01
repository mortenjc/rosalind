import sys, queue
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
n, names, strings = f.readfasta(lines)
#all = Path(filename).read_text()

s = strings[0]
ls = len(s)
p = [0] * ls

i, l = KMP_search('CAGCATGGTATCACAGCAGAG', 'CAGCA')
print(i, l)

# for j in range(1,ls-1):
#     s1 = s[0:ls-2]
#     pat = s[j+1:]
#     print(s1, pat)
#     print(KMP_search(s[0:j], s[j+1:]))
