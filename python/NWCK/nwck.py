import sys, queue
from pathlib import Path
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


def tree_to_list(tree):
    s2 = tree.replace('(', '[')
    s3 = s2.replace(')', '],')
    s4 = s3.replace(';', '')
    return '[' + s4 + ', root]'

#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(filename)
#lines = f.readlines(filename)
all = Path(filename).read_text()

a = all.split('\n\n')

for nw in a:
    tree = nw.split('\n')[0]
    dist = nw.split('\n')[1]
    print(tree, tree_to_list(tree))
