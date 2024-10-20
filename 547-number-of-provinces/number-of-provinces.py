class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = {}
        for i in range(0,len(isConnected)):
            parents[i]= i
        edges = []
        for i in range(0,len(isConnected)):
            for j in range(0,len(isConnected)):
                if i!=j and isConnected[i][j] == 1:
                    edges.append([i,j])

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            else:
                pass 
            return parents[x]

        def union(rootx,rooty):
            rootx, rooty = find(rootx), find(rooty)
            if rootx != rooty:
                parents[rooty] = rootx


        for u, v in edges:
            union(u,v)

        unique_components = len(set(find(i) for i in range(len(isConnected))))
        return unique_components