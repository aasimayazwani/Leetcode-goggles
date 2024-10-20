class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        parent = {}
        allwords = sentence1 + sentence2 
        for i in range(0,len(similarPairs)):
            allwords += similarPairs[i]
        allwords = list(set(allwords))
        for word in allwords:
            parent[word] = word

        def find(root):
            if parent[root] != root:
                parent[root] = find(parent[root])
            return parent[root]

        def union(rootx,rooty):
            rootx = find(rootx)
            rooty = find(rooty)

            if rootx != rooty:
                parent[rooty] = rootx
        
        for u, v in similarPairs:
            union(u,v)


        for i in range(0,len(sentence1)):
            if find(parent[sentence1[i]]) != find(parent[sentence2[i]]):
                return False

        return True 
