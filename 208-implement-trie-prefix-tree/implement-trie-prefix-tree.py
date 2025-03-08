class node:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = node()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = node()
            cur = cur.children[c]
        cur.is_end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return cur.is_end_of_word == True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c in cur.children:
                cur = cur.children[c]
            else:
                return False
        return True 

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)