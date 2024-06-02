import sys, math

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#

filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

n = int(lines[0])
arr = list(map(int, lines[1].split(' ')))

assert n == len(arr)
print(n)
print(arr)

swaps = 0
for i in range(2, n):
    k = i
    while k > 0 and arr[k] < arr[k - 1]:
        swaps += 1
        tmp = arr[k]
        arr[k] = arr[k - 1]
        arr[k - 1] = tmp
        k = k - 1
print(arr)
print(swaps)
