class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        parent = {}
        for i in range(0,n+1):
            parent[i] = i 
        rank = [0]*(n+1)
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            nodex, nodey = find(nodex), find(nodey)
            if nodex != nodey:
                if rank[nodex] < rank[nodey]:
                    parent[nodex] = nodey

                elif rank[nodex] > rank[nodey]:
                    parent[nodey] = nodex

                elif rank[nodex] == rank[nodey]:
                    parent[nodey] = nodex
                    rank[nodex] +=1 
                return True

            return False

        connections = sorted(connections,key=lambda x:x[2])
        for k in range(0,len(connections)):
            connections[k][0] -= 1 
            connections[k][1] -= 1
        total_weight = 0 
        length = 0 
        for i in range(0,len(connections)):
            x, y, weight = connections[i]
            if union(x,y):
                total_weight += weight
                length +=1 
                if length == n-1:
                    return total_weight
        return -1 


            
                