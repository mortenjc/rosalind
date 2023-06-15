import sys
sys.path.append('../common')
import toolbox as tb


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'test.txt'

n, names, strings = tb.readfasta(filename)
#print(n, names, strings)

s = strings[0]
for i in range(1,n):
    intron = strings[i]
    s = tb.delintron(s, intron)
#print(s)
print(tb.aminoseq(s))
