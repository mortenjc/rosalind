import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
n, names, strings = f.readfasta(lines)
#print(n, names, strings)

subs = s.substrings(strings[0])
stringlist = strings[:]

for ss in subs:
    if s.matches(stringlist, ss):
        print(f'{ss} matches')
