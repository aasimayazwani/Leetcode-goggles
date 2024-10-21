class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        for i in range(0,n):
            parent[i] = i

        def find(root):
            if root != parent[root]:
                parent[root] = find(parent[root])
            return parent[root]

        def union(rootx,rooty):
            rootx = find(rootx)
            rooty = find(rooty)
            if rootx != rooty:
                parent[rooty] = find(parent[rootx])

        for i in range(0,len(edges)):
            u, v = edges[i][0], edges[i][1]
            union(u,v)
        
        return len(list(set([find(item) for item in list(range(n))])))

            