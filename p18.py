# Implementation of Trie
class Trie():
    def __init__(self):
        self.root = ([],{})
        self.node = self.root

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node[1]:
                node[1][c] = ([],{})
            node = node[1][c]
        node[0].append(word)

    def check(self, ch, from_start):
        if from_start:
            self.node = self.root
        if ch in self.node[1]:
            self.node = self.node[1][ch]
        else:
            return [], False
        return self.node[0], True

trie = Trie()
words = ['hi', 'there', 'him', 'his', 'himself']
# words = ['hi']
for word in words:
    trie.insert(word)

str = ""
edge = {}

# starting from the length of the string
for i in range(len(str)):
    for j in range(i,len(str)):
        wrds, avail = check(str[j], j == i)
        if avail:
            if j not in edge:
                edge[j] = []
            for wrd in wrds:
                edge[j].append( j - len(wrd) )
