import sys, math
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
lines = f.readlines(filename)

assert len(lines) == 2
a = int(lines[1].split()[0])
b = int(lines[1].split()[1])
c = int(lines[1].split()[2])
d = int(lines[1].split()[3])

mystr = lines[0]

print(mystr[a:b+1]+' '+mystr[c:d+1])
