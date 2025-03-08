class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()      

    def addWord(self, word):
        current_node = self.root
        for character in word:
            current_node = current_node.children.setdefault(character, TrieNode())
        current_node.is_word = True
        
    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.is_word
            else:
                ch = word[index]
                if ch == ".":
                    for child in node.children.values():
                        if dfs(child,index+1):
                            return True 
                    return False 

                else:
                    if ch in node.children:
                        return dfs(node.children[ch],index+1)
                    
                    else:
                        return False

        return dfs(self.root,0)

