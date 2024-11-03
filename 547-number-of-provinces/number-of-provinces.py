class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = []
        for i in range(0,len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j] == 1:
                    edges.append([i,j])
    
        parent = {}
        for i in range(0,len(isConnected)):
            parent[i] = i

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            nodex, nodey = find(nodex), find(nodey)
            if nodex != nodey:
                parent[nodey] = nodex  
            
        for x, y  in edges:
            union(x,y)

        return len(set([find(item) for item in range(len(isConnected))]))
