
# Toolbox is a set of utility methods to process integer lists

# Return length of the longest increasing subsequence for a list of integers
def long_incr_sseq(l):
    n = len(l)
    d = [1 for i in range(n)]
    assert len(l) == len(d)

    for i in range(n):
        for j in range(i):
            if l[j] < l[i]:
                d[i] = max(d[i], d[j] + 1)
    return max(d)
