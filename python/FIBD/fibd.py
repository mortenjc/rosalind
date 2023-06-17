import sys
sys.path.append('../common')
import toolbox as tb
import files as f

# https://rosalind.info/problems/fibd

def Fibonaccid(n):
    if n < 0:
        return 0
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonaccid(n-1) + Fibonaccid(n-2) - Fibonaccid(n-3)


def num_rabbits(n, m):
    # n is the n-th month.
    # m is that a rabbit live for m month.
    # in the first month, the num of rabbit is 1.
    num_list = []
    num_list.append(0)
    num_list.append(1)
    for i in range(1, n+1, 1):
        if i < m:
            num_list.append(num_list[i] + num_list[i-1])
        if i == m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m+1])
        if i > m:
            num_list.append(num_list[i] + num_list[i-1] - num_list[i-m])
    return num_list[n]



filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 1

n, d = lines[0].split(' ')
n = int(n)
d = int(d)

#print(fib(6))
print(num_rabbits(n,d))
for i in range(1,6+1):
    print(i, Fibonaccid(i))
