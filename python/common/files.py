
# Collection of file utilities

# Get filename from args, else use default
def filefromargv(argv):
    if len(argv) == 2:
        filename = argv[1]
    else:
        filename = 'test.txt'
    return filename

# Read the file and return lines as a list
def readlines(string):
    f = open(filename, "r")
    data = f.read()
    lines = data.splitlines()
    f.close()
    return lines



# Read a file with multiple sequences in fasta format
def readfasta(filename):
    files = 0
    names = []
    strings = []

    f = open(filename, "r")
    data = f.read()
    lines = data.splitlines()
    tmp = ''
    for l in lines:
        if l[0] == '>':
            if files != 0:
                strings.append(tmp)
            names.append(l[1:])
            files += 1
            tmp =''
        else:
            tmp += l
    strings.append(tmp)
    return files, names, strings
