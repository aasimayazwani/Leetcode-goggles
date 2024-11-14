class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            rootx, rooty = find(nodex), find(nodey)
            if rootx != rooty:
                parent[rooty] = rootx

        edges = []
        parent = {}
        n = len(isConnected)
        for i in range(n):
            parent[i] = i

        for i in range(0,len(isConnected)):
            for j in range(0,len(isConnected[i])):
                if isConnected[i][j] == 1:
                    edges.append([i,j])
        
        for x, y in edges:
            union(x,y)

        return len(set([find(item) for item in range(n)]))

        

        

        
