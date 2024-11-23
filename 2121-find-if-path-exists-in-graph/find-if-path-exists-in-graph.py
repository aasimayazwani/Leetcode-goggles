class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = {}
        for i in range(n):
            parent[i] = i 

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            rootx, rooty = find(nodex), find(nodey)
            if rooty != rootx:
                parent[rooty] = rootx

        for x, y in edges:
            union(x,y)

        for i in range(0,n):
            find(i)

        return find(source) == find(destination)