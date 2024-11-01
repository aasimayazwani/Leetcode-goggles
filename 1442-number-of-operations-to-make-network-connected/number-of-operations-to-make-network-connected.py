class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1 :
            return -1 
        parent = {}
        for i in range(0,n):
            parent[i] = i
        rank = [0]*n

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            nodex, nodey = find(nodex), find(nodey)
            if nodex != nodey:
                if rank[nodex] < rank[nodey]:
                    parent[nodex] = nodey 
                    
                if rank[nodex] > rank[nodey]:
                    parent[nodey] = nodex
                    
                if rank[nodex] == rank[nodey]:
                    parent[nodey] = nodex
                    rank[nodex] +=1 
                    
                return True 
            return False 
        ans = 0
        for x,y in connections:
            union(x,y)    

        components = len(set(find(i) for i in range(n)))
        
        # Minimum operations needed to connect components is components - 1
        return components - 1
        