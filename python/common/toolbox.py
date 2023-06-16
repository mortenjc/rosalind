
# Toolbox is a set of utility methods to process DNA related sequences
from collections import defaultdict

#
## Lookup tables
#

# DNA codons -> Amino acids
codontab = {
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G'
}

# DNA complementation
compltab = {"A" : "T", "T" : "A", "G": "C", "C": "G"}

# calculated from multiplicity
codonmult = {'S': 6, 'F': 2, 'L': 6, 'Y': 2, '*': 3, 'C': 2, 'W': 1, 'P': 4,
           'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2, 'K': 2,
           'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4}


#
## Simple 'string' functions
#

# Reverse a string sequence
def revseq(stringseq):
    return stringseq[::-1]


# Return the amino acid for a DNA nucleotide sequence
def amino(nuclseq):
    assert len(nuclseq) == 3
    return codontab[nuclseq]

# Return the complement to a DNA sequence
def compl(nuclseq):
    s=''
    for i in range(len(nuclseq)):
        s+= compltab[nuclseq[i]]
    return s

#Return the reversed complement to a DNA sequence
def revcompl(nuclseq):
    s=''
    for i in range(len(nuclseq)):
        s+= compltab[nuclseq[i]]
    return revseq(s)

#
## Codon functions
#

def multiplicity():
    s = set()
    d = {}
    for t in codontab:
        amino = codontab[t]
        if amino in s:
            d[amino] += 1
        else:
            s.add(amino)
            d[amino] = 1
    print(d)


# Is this a DNA START codon?
def is_start(seq):
    return seq == 'ATG'

# Is this s DNA STOP codon?
def is_stop(seq):
    return codontab[seq] == '*'

# Return a list, possibly empty, of indexes for START codons
def startcodons(nuclseq):
    pos = []
    for i in range(0, len(nuclseq), 3):
        cod = nuclseq[i:i+3]
        if is_start(cod):
            pos.append(i)
    return pos

# Given a DNA nucleotide sequence string, return the amino acid sequence
def aminoseq(nuclseq):
    s = ''
    for i in range(0, len(nuclseq), 3):
        s += amino(nuclseq[i:i+3])
    return s


#
## Slightly advanced
#

def delintron(string, intron):
    i = string.find(intron)
    if i == -1:
        return string
    s1 = string[:i]
    s2 = string[i+len(intron):]
    return s1 + s2


# Given a DNA nucleotide sequence string, return the amino acid sequence
# between the first START codon (included) and the first STOP codon (excluded)
def openframe(nuclseq):
    state = 0 # 0 initial, 1 started, 2 stopped
    s = ''
    for i in range(0, len(nuclseq), 3):
        codon = nuclseq[i:i+3]
        if len(codon) != 3:
            break
        if state == 0:
            if is_start(codon):
                state = 1
                s = amino(codon)
                continue
        elif state == 1:
                if is_stop(codon):
                    return s
                else:
                    s += amino(codon)
    return ''
