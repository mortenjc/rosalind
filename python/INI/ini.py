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

assert len(lines) == 1

stats = {'A':0, 'C':0, 'G':0, 'T':0}

for i in lines[0]:
    stats[i] += 1

print(stats['A'], stats['C'], stats['G'], stats['T'])
