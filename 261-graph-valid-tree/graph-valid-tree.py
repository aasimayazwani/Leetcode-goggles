class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n-1:
            return False
        
        parent = {}
        rank = [0]*(n)
        for i in range(n):
            parent[i] = i

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            rootx, rooty = find(nodex), find(nodey)
            if rootx != rooty:
                if rank[rooty] >= rank[rootx]:
                    parent[rootx] = rooty
                    rank[rooty] +=1
                else:
                    parent[rooty] = rootx
                    rank[rootx] +=1
                return True
            else:
                return False

        for x, y in edges:
            if union(x,y):
                pass
            else:
                return False
        return True 

