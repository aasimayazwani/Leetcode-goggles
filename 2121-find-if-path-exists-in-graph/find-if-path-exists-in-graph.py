class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = {}
        for i in range(0,n):
            parent[i] = i 

        def find(root):
            if parent[root] != root:
                parent[root] = find(parent[root])
            return parent[root]

        def union(rootx,rooty):
            rootx = find(rootx)
            rooty = find(rooty)

            if rootx != rooty:
                parent[rooty] = rootx

        for x, y in edges:
            union(x,y)

        return find(destination) == find(source)
