class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        for i in range(0,n):
            parent[i] = i
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            nodex, nodey = find(nodex), find(nodey)
            if nodex != nodey:
                parent[nodey] = nodex
        
        for x, y in edges:
            union(x,y)

        return len(set([find(item) for item in range(n)]))