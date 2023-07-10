import sys, math, re
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import graphe

# https://rosalind.info/problems/bfs

filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)


from graphe.digraph import digraph
from graphe.graph import bfs



V, E = list(map(int, lines[0].split()))
DG = digraph.Digraph(V)

for l in lines[1:]:
    e1, e2 = list(map(int, l.split()))
    print(e1,e2)
    DG.add_edge(e1-1, e2-1)

res = []
bfs = bfs.BFSearch(DG, 0)  # make tree with root on vertex 0
for i in range(DG.V):
    bfpath = bfs.path_to(i) # find path to vertex i from 0
    res.append(len(bfpath) - 1)

print('----------')
print(' '.join(list(map(str, res))))

#fig = draw.Draw()
#fig.node_attr(label='')
#fig.draw(G, bfpath)
