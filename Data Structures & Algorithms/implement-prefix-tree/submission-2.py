class Node:
    
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for i,c in enumerate(word):
            idx = ord(c)-ord('a')
            if idx not in curr.children:
                curr.children[idx] = Node()
            curr = curr.children[idx]
            if i == len(word)-1:
                curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for i,c in enumerate(word):
            idx = ord(c)-ord('a')
            if idx not in curr.children:
                return False
            curr = curr.children[idx]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for i,c in enumerate(prefix):
            idx = ord(c)-ord('a')
            if idx not in curr.children:
                return False
            curr = curr.children[idx]
        return True
        