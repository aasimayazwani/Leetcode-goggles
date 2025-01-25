class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = {}
        for i in range(0,n):
            parent[i] = i

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            rootx, rooty = find(nodex),find(nodey)
            if rootx != rooty:
                parent[rootx] = rooty
        
        for x,y in edges:
            union(x,y)

        for i in range(0,n):
            find(i)

        return parent[source] == parent[destination]