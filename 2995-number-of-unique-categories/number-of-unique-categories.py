# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:
        graph = {}
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                if categoryHandler.haveSameCategory(i,j):
                    edges.append([i,j])
        parents = {}
        for i in range(n):
            parents[i] = i

        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            return parents[node]

        def union(nodex, nodey):
            rootx, rooty = find(nodex), find(nodey)
            if rootx != rooty:
                parents[rooty] = rootx

        for x, y in edges:
            union(x,y)

        return len(set([find(item) for item in range(n)]))