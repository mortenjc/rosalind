# Collection of file utilities


# Get filename from args, else use default
def filefromargv(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'test.txt'
    return filename


# Read the file and return lines as a list
def readlines(filename):
    f = open(filename, "r")
    data = f.read()
    lines = data.splitlines()
    f.close()
    return lines


# Read a file with multiple sequences in fasta format
def readfasta(lines):
    files = 0
    names = []
    strings = []

    tmp = ''
    for l in lines:
        if l[0] == '>':
            if files != 0:
                strings.append(tmp)
            names.append(l[1:])
            files += 1
            tmp = ''
        else:
            tmp += l
    strings.append(tmp)
    return files, names, strings


# Read a lines with multiple sequences in fastq format
def readfastq(lines):
    n = 0
    name = []
    seq = []
    qual = []

    assert len(lines) % 4 == 0

    n = len(lines) // 4
    for i in range(0, len(lines), 4):
        l0 = lines[i + 0]
        l1 = lines[i + 1]
        l2 = lines[i + 2]
        l3 = lines[i + 3]
        assert l0[0] == '@'
        name.append(l0[1:])
        assert l1[0] in 'ATGC'
        seq.append(l1)
        assert l2[0] == '+'
        assert l3[0] >= '!' and l3[0] <= '~'
        assert len(l3) == len(l1)
        qual.append(l3)

    return n, name, seq, qual
