class Node:
    def __init__(self):
        self.children = {}
        self.word = None

class Trie:
    def __init__(self):
        self.root = Node()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.word = word

    def hasWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.word is not None



if __name__ == "__main__":
    words = ["swiss", "china", "hello", "world"]
    trie = Trie()
    for word in words:
        trie.addWord(word)

    for word in ["swi", "swiss", "h", "world"]:
        print(word, trie.hasWord(word))



