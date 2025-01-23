class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def find(node):
            if parent[node] !=node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            rootx, rooty =find(nodex), find(nodey)
            if rootx != rooty:
                parent[rootx] = rooty
        
        parent = {}
        for i in range(0,n):
            parent[i] = i

        for x,y in edges:
            union(x,y)

        for i in range(0,n):
            parent[i] = find(i)

        return len(list(set(parent.values())))
