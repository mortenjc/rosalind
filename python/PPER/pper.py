import sys, math

sys.path.append('../common')
import toolbox as tb
import files as f

# https://rosalind.info/problems/fibd


def pper(n, k):
    return math.factorial(n) // math.factorial(n - k)


filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

assert len(lines) == 1

n, k = lines[0].split(' ')
n = int(n)
k = int(k)

print(f'n={n}, k={k}')
print(pper(n, k))
print(pper(n, k) % 1000000)
