import sys, math
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s



def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)


#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 1
n = int(lines[0].split()[0])
assert n <= 25
print(n)
print(fib(n))
