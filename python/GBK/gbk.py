import sys, math

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


#
# #
#

filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

assert len(lines) == 3
name = lines[0]
date_from = lines[1]
date_to = lines[2]

print(name)
print(date_from)
print(date_to)

query = f'"{name}"[Organism] AND ("{date_from}"[PDAT] : "{date_to}"[PDAT])'

print(query)

from Bio import Entrez

Entrez.email = "mortenjc@jcaps.com"
handle = Entrez.esearch(db="nucleotide", term=query)
record = Entrez.read(handle)
print(record['Count'])
