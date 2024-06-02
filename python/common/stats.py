import math


# Bernoulli distribution
# n number of Bernoulli trials
# p probability of outcome
# k number of occurences of outcome
def bern(n, k, p):
    assert p <= 1.0
    q = 1.0 - p
    return math.comb(n, k) * p**k * q ** (n - k)


# integrate (sum) values from k up to n of bern(n,k,p)
def berni(n, k, p):
    res = 0.0
    for i in range(k, n + 1):
        print(i)
        res += bern(n, i, p)
    return res
