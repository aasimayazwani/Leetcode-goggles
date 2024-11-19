class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges= []
        for i in range(0,len(isConnected)):
            for j in range(i+1,len(isConnected)):
                if isConnected[i][j] == 1:
                    edges.append([i,j])
        n = len(isConnected)
        parent = {}
        for i in range(0,n):
            parent[i] = i
        
        def find(root):
            if parent[root] != root:
                parent[root] = find(parent[root])
            return parent[root]
        
        def union(nodex,nodey):
            rootx, rooty= find(nodex), find(nodey)
            if rootx != rooty:
                parent[rooty] = rootx
            
        for x, y in edges:
            union(x,y)

        return len(set([find(item) for item in range(n)]))