class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence2) != len(sentence1):
            return False
        edges = similarPairs
        parent = {}
        pairs = sentence1 + sentence2 
        for i in range(0,len(edges)):
            pairs.extend(edges[i])
        pairs = list(set(pairs))
        for i in range(0,len(pairs)):
            parent[pairs[i]] = pairs[i]
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            rootx, rooty = find(nodex), find(nodey)
            if rootx != rooty:
                parent[rooty] = rootx
            
        for x, y in edges:
            union(x,y)

         
        keys = list(parent.keys())
        for i in range(0,len(keys)):
            parent[keys[i]] = find(keys[i])
        
        for i in range(0,len(sentence1)):
            if find(sentence2[i]) != find(sentence1[i]):
                return False
        return True 
                    