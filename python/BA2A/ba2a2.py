import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import copy

# https://rosalind.info/problems/ba1a

#
# #
#


def getkmers(s1, k):
    res = set()
    for i in range(len(s1) - k + 1):
        kmer = s1[i:i+k]
        assert len(kmer) == k
        res.add(kmer)
    return list(res)

def diffn(s1, s2, n):
    assert len(s1) == len(s2)
    diffs = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diffs += 1
    if diffs <= n:
        return True
    return False


def motEnum(Dna, k, d):
    Patterns = set()



filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, names, seqs, qual = f.readfastq(lines[1:])

k, d = map(int, lines[0].split())
seqs = lines[1:]

print(k,d)
print(seqs)

# MOTIFENUMERATION(Dna, k, d)
#     Patterns ← an empty set
#     for each k-mer Pattern in Dna
#         for each k-mer Pattern’ differing from Pattern by at most d mismatches
#             if Pattern' appears in each string from Dna with at most d mismatches
#                 add Pattern' to Patterns
#     remove duplicates from Patterns
#     return Patterns
