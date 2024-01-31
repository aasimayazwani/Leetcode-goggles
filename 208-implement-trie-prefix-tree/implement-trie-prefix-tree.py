class Trie:

    def __init__(self):
        self.words = {}
        self.prefix = {}

    def insert(self, word: str) -> None:
        self.words[word] = 1  

    def search(self, word: str) -> bool:
        if word in self.words:
            return True 
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if prefix in set([item[0:len(prefix)] for item in list(self.words.keys())]):
            return True 
        else:
            return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)