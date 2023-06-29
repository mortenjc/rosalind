import sys, math
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


def bsearch(arr, key):
    left = 0
    right = len(arr) - 1

    while True:
        if right == left:
            if  arr[right] == key:
                return right + 1
            else:
                return -1

        i = (left + right)//2
        #print(f'[{left}, {i}, {right}]')
        if arr[i] == key:
            #print(f'match {i}')
            return i + 1
        elif key < arr[i]:
            #print(f'left')
            right = i
        else:
            #print(f'right')
            left = i + 1



#
# #
#

filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 4

slen = int(lines[0])
klen = int(lines[1])
sorted = list(map(int, lines[2].split(' ')))
keys = list(map(int, lines[3].split(' ')))

print(sorted)
res = []
for key in keys:
    print('search for', key)
    res.append(bsearch(sorted, key))
print(' '.join(list(map(str,res))))
