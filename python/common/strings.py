# Toolbox is a set of utility methods to process DNA related sequences

import numpy as np

# Reverse a string
def reverse(stringseq):
    return stringseq[::-1]


# generate all substrings of a string
def substrings(string):
    l = len(string)
    if l <= 1:
        return []
    myset = set()
    for i in range(2, l+1):
        for j in range(l - i + 1):
            ss = string[j:i+j]
            myset.add(ss)
    mylist = list(myset)
    mylist.sort()
    return mylist


# return all indexes of matches
def findall(string, pattern):
    start = 0
    pos = []
    for i in range(len(string)):
        if string[i:i+len(pattern)] == pattern:
            pos.append(i+1)
    return pos


# Count the number of contiguous matches between two strings
# where s2 is 'offset' from s1 by a specified amount
#
# For example: (ABCDEF, 3, DEFXYZ) has three overlaps (DEF) at offset 3
#    ABCDEF
#       DEFXYZ
def contiguous_matches(s1, offset, s2):
    matches = 0
    #print(s1, offset, s2)
    minlen = min(len(s1) - offset, len(s2))
    #print('minlen', minlen)
    for i in range(minlen):
        #print(i, s1[i+offset], s2[i])
        if s1[i + offset] != s2[i]:
            break
        else:
            matches += 1
    return matches


# Is seq a subsequence of s?
def issubseq(s, seq):
    i = 0
    j = 0
    while i < len(seq):
        if i == len(seq) or j == len(s):
            break
        if seq[i] == s[j]:
            i+=1
            j+=1
        else:
            j+=1

    if i == len(seq):
        return True
    else:
        return False

# Find length of longes common substring of two strings
# Adapted to python from
# https://en.wikipedia.org/wiki/Longest_common_subsequence
def lcs_length(X, Y):
    print(X)
    print()
    print(Y)
    m = len(X)
    n = len(Y)
    C = np.ndarray((m+1, n+1))
    for i in range(m+1):
        C[i,0] = 0
    for j in range(n+1):
        C[0,j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                C[i,j] = C[i-1,j-1] + 1
            else:
                C[i,j] = max(C[i,j-1], C[i-1,j])
    return C, int(C[m,n])


# Return one longest common substring
# Adapted to python from
# https://en.wikipedia.org/wiki/Longest_common_subsequence
def lcs_backtrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    if  X[i-1] == Y[j-1]:
        return lcs_backtrack(C, X, Y, i-1, j-1) + X[i-1]
    if C[i,j-1] > C[i-1,j]:
        return lcs_backtrack(C, X, Y, i, j-1)
    return lcs_backtrack(C, X, Y, i-1, j)


# find the longest overlap between two strings s1 and s2
# returns the index of the overlap and the size
def longest_overlap(s1, s2):
    longest = 0
    longesti = 0
    for i in range(len(s1)):
        ovlcount = contiguous_matches(s1, i, s2)
        if ovlcount > longest:
            longest = ovlcount
            longesti = i

    return (longesti, longest)



# check if pattern occurs in a list of strings
def matches(strings, pattern):
    for string in strings:
        #print(f'search for {ss} in {string}')
        if string.find(pattern) == -1:
            return False
    return True


# return all permutations of string
def permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]

    l = []
    for i in range(len(lst)):
        m = lst[i]
        remlst = lst[:i] + lst[i+1:]

        for p in permutations(remlst):
            l.append(m + p)
    return l


# return a list of floats from a line
def tofloat(str, sep=' '):
    return list(map(float, str.split(sep)))

# return a list of ints from a line
def toint(str, sep=' '):
    return list(map(int, str.split(sep)))
