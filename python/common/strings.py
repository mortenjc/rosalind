
# Toolbox is a set of utility methods to process DNA related sequences


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
