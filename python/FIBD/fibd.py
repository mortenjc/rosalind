import sys

sys.path.append('../common')
import toolbox as tb
import files as f

# https://rosalind.info/problems/fibd


def rabbits(n, d):
    s = set()
    s.add(0)
    s.add(1)
    sd = {0: 1, 1: 1}

    def Fibonaccid(n, d):
        if n in s:
            # print(s)
            return sd[n]
        if n == 1 or n == 2:
            return 1
        elif n < d:
            f = Fibonaccid(n - 1, d) + Fibonaccid(n - 2, d)
            s.add(n)
            sd[n] = f
            return f
        elif n == d:
            f = Fibonaccid(n - 1, d) + Fibonaccid(n - 2, d) - 1
            s.add(n)
            sd[n] = f
            return f
        else:
            f = Fibonaccid(n - d, d) + Fibonaccid(n - d - 1, d)
            s.add(n)
            sd[n] = f
            return f

    return Fibonaccid(n, d)


filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

assert len(lines) == 1

n, d = lines[0].split(' ')
n = int(n)
d = int(d)

print(n, d)
f = rabbits(n, d)
print(f)
print('----')

# print(fib(6))
# print(num_rabbits(n,d))
# for i in range(1,6+1):
#    print(i, rabbits(i,3))


def tests(n, d, r):
    print(n, d, r, '-', rabbits(n, d))


tests(6, 3, 4)
tests(12, 3, 71)
tests(25, 31, 75025)
