class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = {}
        rank = [0]*len(points)
        for i in range(0,len(points)):
            parent[i] = i
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            nodex, nodey = find(nodex), find(nodey)
            if nodex != nodey:
                if rank[nodex] > rank[nodey]:
                    parent[nodey] = nodex

                elif rank[nodex] < rank[nodey]:
                    parent[nodex] = nodey

                elif rank[nodex] == rank[nodey]:
                    parent[nodey] = nodex
                    rank[nodex] +=1 
                return True 
            return False

        edges = []
        target = len(points)-1
        visited = 0
        for i in range(0,len(points)):
            for j in range(i+1,len(points)):
                distance = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
                edges.append([distance,i,j])
        edges = sorted(edges,key=lambda x:x[0])
        total_distance = 0
        for i in range(0,len(edges)):
            dist, x, y = edges[i]
            if union(x,y):
                total_distance += dist
                visited +=1 
                if visited == target:
                    break
            else:
                pass 
        return total_distance 
        
