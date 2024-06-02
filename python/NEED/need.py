import sys

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#
from Bio import Entrez


def getfasta(name):
    Entrez.email = "mortenjc@jcapd.com"
    handle = Entrez.efetch(db="nucleotide", id=name, rettype="fasta")
    record = handle.read()
    assert record[0] == '>'
    tmp = record.split('\n')
    return tmp[0], ''.join(tmp[1:])


filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
# print(n, names, strings)
lines = f.readlines(filename)
assert len(lines) == 1
assert len(lines[0].split()) == 2
n1, n2 = lines[0].split()

f1h, f1n = getfasta(n1)
print(f1n)

print()

f2h, f2n = getfasta(n2)
print(f2n)

# Then use this page (DNA option), more options set gap penalty
# https://www.ebi.ac.uk/jdispatcher/psa/emboss_needle
