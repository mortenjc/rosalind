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


lineno = 1
for i in range(len(lines)):
    if lineno & 0x1 == 0:
        print(lines[i])
    lineno+=1
