# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        edges = []
        for i in range(n):
            for j in range(i,n):
                if categoryHandler.haveSameCategory(i,j):
                    edges.append([i,j])
        parent = {}
        for i in range(n):
            parent[i] = i 
    
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            nodex, nodey = find(nodex), find(nodey)
            if nodex != nodey:
                parent[nodey] = nodex
        
        for x,y in edges:
            union(x,y)

        return len(set([find(item) for item in range(n)]))
        