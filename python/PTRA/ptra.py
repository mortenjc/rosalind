import sys, math, re
from Bio.Seq import translate
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import stats as st

# https://rosalind.info/problems/ptra
# http://www.bioinformatics.org/JaMBW/2/3/TranslationTables.html

#
# #
#

filename = f.filefromargv(sys.argv)
lines = f.readlines(filename)
#n, name, seqs, qual = f.readfastq(lines[1:])

assert len(lines) == 2

seq = lines[0]
pro = lines[1]

print(seq)
print(pro)
print('----------')

for i in [1,2,3,4,5,6,9,10,11,12,13,14,15]:
    res = translate(seq, table=i, to_stop=True)
    if pro == res:
        print(i)
