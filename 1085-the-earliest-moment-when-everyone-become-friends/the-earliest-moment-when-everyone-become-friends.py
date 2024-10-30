class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs,key=lambda x:x[0])
        parent = {}
        for i in range(0,n):
            parent[i] = i
        rank = [0]*(n)

        visited_components = n

        def find(root):
            if parent[root] != root:
                parent[root] = find(parent[root])
            return parent[root]

        def union(time,rootx,rooty):
            nonlocal visited_components
            rootx, rooty =find(rootx), find(rooty)
            if rootx != rooty:
                if rank[rootx] < rank[rooty]:
                    parent[rootx] = rooty
                
                elif rank[rootx] > rank[rooty]:
                    parent[rooty] = rootx
                
                elif rank[rootx] == rank[rooty]:
                    parent[rooty] = rootx
                    rank[rootx] +=1 
                    
                visited_components -=1 
                
                if visited_components == 1:
                    return time
        for time, x, y in logs:
            result = union(time, x, y)
            if result is not None:
                return result
        return -1
                        