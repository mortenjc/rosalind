
# Toolbox is a set of utility methods to process DNA related sequences

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
