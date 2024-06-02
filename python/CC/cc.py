import sys

sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


class CC:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFS_Utililty(self, temp, v, visited):

        visited[v] = True

        temp.append(v)

        for i in self.adj[v]:
            if visited[i] == False:
                temp = self.DFS_Utililty(temp, i, visited)
        return temp

    def add_edge(self, v, w):
        print(v, w)
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connected_components(self):
        visited = []
        conn_compnent = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                conn_compnent.append(self.DFS_Utililty(temp, v, visited))
        return conn_compnent


#
# #
#


filename = f.filefromargv(sys.argv)
# n, names, strings = f.readfasta(lines)
# print(n, names, strings)
lines = f.readlines(filename)

V = int(lines[0].split(' ')[0])
NE = int(lines[0].split(' ')[1])
E = []
for i in range(len(lines) - 1):
    E.append(list(map(int, lines[i + 1].split())))
print(V, E)

mycc = CC(V)
for edge in E:
    mycc.add_edge(edge[0] - 1, edge[1] - 1)

ccomp = mycc.connected_components()
print(ccomp)
print(len(ccomp))
