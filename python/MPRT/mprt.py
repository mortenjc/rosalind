import sys, re

sys.path.append('../common')
import toolbox as tb
import urllib.request


def namecut(longname):
    i = longname.find('_')
    if i == -1:
        return longname
    else:
        return longname[:i]


def search(patt, string):
    res = patt.match(string)
    if res:
        return True
    return False


# extract the canonical (?) name from the fasta header
def getname(header):
    # print(header)
    res = re.search('^.*\|(.+)\|.*', header)
    return res.group(1)


def getdata(protid):
    try:
        req = f'https://rest.uniprot.org/uniprotkb/{protid}.fasta'
        # print(req)
        with urllib.request.urlopen(req) as response:
            text = response.read()
            text = text.decode('ascii').split('\n')
            return text[0], "".join(text[1:])
    except:
        return '', ''


# problem: https://rosalind.info/problems/mprt
# rest api for data: https://rest.uniprot.org/uniprotkb/B5ZC00.fasta

# s N{P}[ST]{P}.
# pattern = re.compile('N[^P][ST][^P]')
pattern = re.compile('N[^P][ST][^P]')


if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'test.txt'

f = open(filename, "r")
data = f.read()
lines = data.splitlines()
f.close()

for prot in lines:
    protname = namecut(prot)
    header, seq = getdata(protname)
    if header == '':
        print(f'No file for {prot}')
        continue
    # name = getname(header)
    # if name != protname:
    # print(f'new name {protname}->{name}')

    res = ''
    for i in range(len(seq)):
        string = seq[i:]
        if search(pattern, string):
            res += f'{i+1} '
    print(prot)
    if res != '':
        print(res[:-1])
    else:
        print()
