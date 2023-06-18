
# Toolbox is a set of utility methods to process integer lists


# return list of integers from list of str
def listofint(l):
    assert isinstance(l[0], str), 'first element of list is not a str'
    return list(map(int, l))


# return list of str from list of int
def listofstr(l):
    assert isinstance(l[0], int), 'first element of list is not an int'
    return list(map(str, l))


# Return (one) of) the longest increasing/decreasing subsequences for a list of
# integers https://cp-algorithms.com/sequences/longest_increasing_subsequence.html
def long_sseq(l, increase=True):
    assert isinstance(l[0], int), "first element of list is not an int"
    n = len(l)
    d = [1 for i in range(n)]
    p = [-1 for i in range(n)]

    for i in range(n):
        for j in range(i):
            if increase:
                if l[j] < l[i] and d[i] < d[j] + 1:
                    d[i] = d[j] + 1
                    p[i] = j
            else:
                if l[j] > l[i] and d[i] < d[j] + 1:
                    d[i] = d[j] + 1
                    p[i] = j
    res = d[0]
    pos = 0
    for i in range(1,n):
        if d[i] > res:
            res = d[i]
            pos = i
    r = []
    while pos != -1:
        r.append(l[pos])
        pos = p[pos]
    return r[::-1]
