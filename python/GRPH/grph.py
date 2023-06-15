import sys
sys.path.append('../common')
import toolbox as tb


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'test.txt'

n, names, strings = tb.readfasta(filename)
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
