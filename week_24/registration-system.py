class Node:
    def __init__(self):
        self.children = {}
        self.name = ''
        self.suffix = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def request(self, name):
        node = self.root
        for c in name:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]

        if not node.name:
            print('OK')
            node.name = name
        else:
            node.suffix += 1
            print(node.name + str(node.suffix))

trie = Trie()
t = int(input())
for _ in range(t):
    name = input()
    trie.request(name)
    