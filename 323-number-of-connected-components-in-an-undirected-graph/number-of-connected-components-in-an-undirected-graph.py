class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = {}
        for i in range(0,n):
            parent[i] = i
            
        def find(root):
            if parent[root] != root:
                parent[root] = find(parent[root])
            else:
                pass 
            return parent[root]

        def union(rootx,rooty):
            rootx = find(rootx)
            rooty = find(rooty)
            
            if rootx != rooty:
                parent[rooty] = rootx
                
        for x, y in edges:
            union(x,y)

        cur = [find(i) for i in list(range(n))]
        return len(list(set(cur)))