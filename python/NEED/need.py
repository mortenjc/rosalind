import sys
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(lines)
#print(n, names, strings)
lines = f.readlines(filename)

assert len(lines) == 1

id = f'"{lines[0]}"'

from Bio import Entrez
Entrez.email = "mortenjc@jcapd.com"
handle = Entrez.efetch(db="nucleotide", id=[id], rettype="fasta")
records = handle.read().split('\n')

print(records)
