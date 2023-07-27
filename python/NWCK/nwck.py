import sys, queue
from pathlib import Path
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s
import random

from graphe.graph import graph
from graphe.graph import bfs

# iterator to produce a new incrementing number on every call
def number():
    num = 1
    while True:
        yield num
        num = num + 1

numb = number()


# separate right node from left nodes
def separate(s1):
    assert s1[0] == '('
    end = s1.rfind(')')
    return s1[1:end], s1[end+1:]


# run through left nodes and create dummy nodes when necessary
def split(s1):
    par = 0
    nod = ''
    nodes = []
    for i in range(len(s1)):
        c = s1[i]
        if c == '(':
            par += 1
            nod += c
            continue
        if c == ')':
            par -= 1
            nod += c
            continue
        if c == ',':
            if par == 0:
                if len(nod) == 0:
                    nod = 'a'+str(next(numb))
                nodes.append(nod)
                nod =''
                continue
            else:
                nod += c
        else:
            nod += c
    if len(nod) == 0:
        nod = 'a'+str(next(numb))
    nodes.append(nod)
    return nodes


def pathto(nodes, v, n1, n2):
    V = len(nodes)
    G = graph.Graph(V)

    for l in v:
        e1 = nodes[l[0]]
        e2 = nodes[l[1]]
        G.add_edge(e1, e2)

    res = []
    bfs2 = bfs.BFSearch(G, nodes[n1])
    bfpath = bfs2.path_to(nodes[n2])
    return bfpath


def netwick(tree):
    seen = set()
    nodes = {}
    v = []

    def addnode(nod):
        if not nod in seen:
            seen.add(nod)
            nodes[nod] = len(nodes)

    def adddummynode():
        dnode = 'n' + str(next(numb))
        if not dnode in seen:
            nodes[dnode] = len(nodes)
            seen.add(dnode)
        return dnode

    def parsetree(tree):
        subt, rnode = separate(tree)

        # call ';' root, else ignore ';'
        if rnode == ';':
            rnode = 'root'
        else:
            if rnode[-1] == ';':
                rnode = rnode[:-1]
        addnode(rnode)

        res = split(subt)
        for lnode in res:
            assert len(lnode) != 0
            if lnode[0] == '(' and lnode[-1] == ')':
                dn = adddummynode()
                v.append([dn, rnode])
                parsetree(lnode+dn)
            elif lnode[0] == '(' and lnode[-1] != ')':
                a,b = separate(lnode)
                v.append([b, rnode])
                parsetree(lnode)
            else:
                addnode(lnode)
                v.append([lnode, rnode])
    parsetree(tree)
    return v, nodes

#
# #
#

filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(lines)
#lines = f.readlines(filename)
all = Path(filename).read_text()

dists = []
a = all.split('\n\n')
for nw in a:
    tree = nw.split('\n')[0]
    dist = nw.split('\n')[1].split()
    assert len(dist) == 2

    v, nodes = netwick(tree)

    res = pathto(nodes, v, dist[0], dist[1])
    dists.append(str(len(res)-1))

print(' '.join(dists))
