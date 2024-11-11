class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {}
        n = len(s)
        for i in range(0,n):
            parent[i] = i
        
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex, nodey):
            rootX = find(nodex)
            rootY = find(nodey)
            if rootX != rootY:
                parent[rootY] = rootX

        for x, y in pairs:
            union(x,y)

        for i in range(0,n):
            find(i)

        from collections import defaultdict
        compounds = defaultdict(list)
        for i in range(n):
            root = find(i)
            compounds[root].append(i)
        
        answer = [item for item in s]
        for indices in compounds.values():
            sorted_characters = sorted([s[item] for item in indices])
            for idex in indices:
                answer[idex] = sorted_characters[0]
                sorted_characters.pop(0)
        return "".join(answer)