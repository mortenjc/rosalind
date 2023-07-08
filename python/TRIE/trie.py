import sys, queue
sys.path.append('../common')
import toolbox as tb
import files as f
import strings as s


# With modification from
# https://albertauyeung.github.io/2020/06/15/python-trie.html/
class TrieNode:
    def __init__(self, char, prev, n):
        self.char = char
        self.prev = prev
        self.n = n
        self.is_end = False
        self.counter = 0
        self.children = {}


class Trie(object):
    def __init__(self):
        self.n = 0
        self.root = TrieNode("", -1, self.n)


    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # character is not found, create node
                self.n += 1
                new_node = TrieNode(char, node.n, self.n)
                node.children[char] = new_node
                node = new_node

        node.is_end = True # end of a word
        node.counter += 1


    def traverse(self):
        q = queue.Queue()
        q.put(self.root)
        while not q.empty():
            node = q.get(False)
            if node.prev != -1:
                print(node.prev+1, node.n+1, node.char)
            for char in node.children:
                newnode = node.children[char]
                q.put(newnode)

#
# #
#


filename = f.filefromargv(sys.argv)
#n, names, strings = f.readfasta(lines)
lines = f.readlines(filename)

t = Trie()
for word in lines:
    t.insert(word)

t.traverse()
