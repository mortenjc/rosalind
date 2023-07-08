import sys
sys.path.append('../common')
import toolbox as tb
import files as f


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, strings = f.readfasta(lines)
#print(n, names, strings)

s = strings[0]
for i in range(1,n):
    intron = strings[i]
    s = tb.delintron(s, intron)
#print(s)
print(tb.aminoseq(s))
