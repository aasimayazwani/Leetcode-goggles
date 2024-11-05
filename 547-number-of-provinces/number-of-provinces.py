class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(nodex):
            if parent[nodex] != nodex:
                parent[nodex] = find(parent[nodex])
            return parent[nodex]

        def union(nodex, nodey):
            nodex, nodey = find(nodex), find(nodey)
            if nodex != nodey:
                parent[nodey] = nodex
        edges = []
        for i in range(0,len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j] == 1:
                    edges.append([i,j])
        parent = {}
        for i in range(len(isConnected)):
            parent[i] = i

        for x,y in edges:
            union(x,y)
        
        return len(set([find(item) for item in range(len(isConnected))]))
            