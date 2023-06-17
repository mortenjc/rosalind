
# Toolbox is a set of utility methods to process integer lists


# Return (one) of) the longest increasing subsequence for a list of integers
# https://cp-algorithms.com/sequences/longest_increasing_subsequence.html
def long_incr_sseq(l):
    n = len(l)
    d = [1 for i in range(n)]
    p = [-1 for i in range(n)]
    assert len(l) == len(d)

    for i in range(n):
        for j in range(i):
            if l[j] < l[i] and d[i] < d[j] + 1:
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
