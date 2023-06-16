import sys
sys.path.append('../common')
import toolbox as tb
import files as f


filename = f.filefromargv(sys.argv)
n, names, strings = f.readfasta(filename)
#print(n, names, strings)

for i in range(n):
    last = strings[i][-3:]
    for j in range(n):
        if i == j:
            continue
        first =  strings[j][:3]
        if last == first:
            assert names[i] != names[j]
            print(f'{names[i]} {names[j]}')
