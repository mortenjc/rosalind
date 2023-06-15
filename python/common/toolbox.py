



codontab = {
    'TCA': 'S',    'TCC': 'S',    'TCG': 'S',    'TCT': 'S',
    'TTC': 'F',    'TTT': 'F',    'TTA': 'L',    'TTG': 'L',
    'TAC': 'Y',    'TAT': 'Y',    'TAA': '*',    'TAG': '*',
    'TGC': 'C',    'TGT': 'C',    'TGA': '*',    'TGG': 'W',
    'CTA': 'L',    'CTC': 'L',    'CTG': 'L',    'CTT': 'L',
    'CCA': 'P',    'CCC': 'P',    'CCG': 'P',    'CCT': 'P',
    'CAC': 'H',    'CAT': 'H',    'CAA': 'Q',    'CAG': 'Q',
    'CGA': 'R',    'CGC': 'R',    'CGG': 'R',    'CGT': 'R',
    'ATA': 'I',    'ATC': 'I',    'ATT': 'I',    'ATG': 'M',
    'ACA': 'T',    'ACC': 'T',    'ACG': 'T',    'ACT': 'T',
    'AAC': 'N',    'AAT': 'N',    'AAA': 'K',    'AAG': 'K',
    'AGC': 'S',    'AGT': 'S',    'AGA': 'R',    'AGG': 'R',
    'GTA': 'V',    'GTC': 'V',    'GTG': 'V',    'GTT': 'V',
    'GCA': 'A',    'GCC': 'A',    'GCG': 'A',    'GCT': 'A',
    'GAC': 'D',    'GAT': 'D',    'GAA': 'E',    'GAG': 'E',
    'GGA': 'G',    'GGC': 'G',    'GGG': 'G',    'GGT': 'G'
}

comptab = {"A" : "T", "T" : "A", "G": "C", "C": "G"}


def amino(seq):
    assert len(seq) == 3
    return codontab[seq]


def is_start(seq):
    return seq == 'AUG' or seq == 'ATG'


def is_stop(seq):
    return codontab[seq] == '*'


def startpositions(string):
    pos = []
    for i in range(0, len(string), 3):
        cod = string[i:i+3]
        if is_start(cod):
            pos.append(i)
    return pos


# Read a file with multiple sequences in fasta format
def readfasta(filename):
    files = -1
    names = []
    strings = []

    f = open(filename, "r")
    data = f.read()
    lines = data.splitlines()
    tmp = ''
    for l in lines:
        if l[0] == '>':
            if files != -1:
                strings.append(tmp)
            names.append(l[1:])
            files += 1
            tmp =''
        else:
            tmp += l
    strings.append(tmp)
    return files, names, strings


# reverse a sequence string
def revseq(string):
    return string[::-1]


def compl(string):
    s=''
    for i in range(len(string)):
        s+= comptab[string[i]]
    return s


def revcompl(string):
    s=''
    for i in range(len(string)):
        s+= comptab[string[i]]
    return revseq(s)


def aminoseq(dnastr):
    s = ''
    for i in range(0, len(dnastr), 3):
        s += amino(dnastr[i:i+3])
    return s
