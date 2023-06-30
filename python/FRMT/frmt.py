import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
#print(n, names, strings)
lines = f.readlines(filename)

assert len(lines) == 1

id = f'"{lines[0]}"'

from Bio import Entrez
Entrez.email = "mortenjc@jcapd.com"
handle = Entrez.efetch(db="nucleotide", id=[id], rettype="fasta")
records = handle.read().split('\n')

names = []
strings = []
res = ''
for i in records:
    if i == '':
        continue
    if i[0] == '>':
        names.append(i)
        if res != '':
            strings.append(res)
        res = ''
    else:
        res += i
strings.append(res)

minval = 1000000000
minidx = -1
for i, seq in enumerate(strings):
    if len(seq) < minval:
        minval = len(seq)
        minidx = i

print(names[minidx])
res = ''
for i in range(len(strings[minidx])):
    res += strings[minidx][i]
    if (i+1) % 70 == 0:
        print(res)
        res = ''
print(res)
