class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges  = []
        for i in range(0,len(points)):
            for j in range(i+1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) 
                edges.append([i,j,dist])

        edges = sorted(edges,key = lambda x:x[2])
        
        parent = {}
        n = len(points)
        rank = [0]*(n)
        for i in range(n):
            parent[i] = i

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex, nodey):
            rootx, rooty = find(nodex), find(nodey)
            if rootx != rooty:
                if rank[rootx] < rank[rooty]:
                    parent[rootx] = rooty
                    rank[rooty] +=1

                elif rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                    rank[rootx] +=1 

                elif rank[rootx] == rank[rooty]:
                    rank[rootx] +=1 
                    parent[rooty] = rootx
                
                return True 
            return False
            
        total = 0
        for x,y, cost in edges:
            if union(x,y):
                total += cost
        return total 