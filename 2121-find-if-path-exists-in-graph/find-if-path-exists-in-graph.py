class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = {}
        for i in range(0,n):
            parent[i] = i

        def find(root):
            if  parent[root] != root:
                parent[root] = find(parent[root])
            return parent[root]

        def union(root1,root2):
            root1 = find(root1)
            root2 = find(root2)
            if root1 != root2:
                parent[root2] = root1

        for i in range(0,len(edges)):
            union(edges[i][0],edges[i][1])
            
        return find(source) == find(destination)
        