class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs = sorted(logs,key=lambda x:x[0])
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex,nodey):
            rootx, rooty = find(nodex), find(nodey)
            if rootx != rooty:
                if rank[rootx] >= rank[rooty]:
                    parent[rooty] = rootx
                    rank[rootx] +=1
                else:
                    parent[rootx] = rooty
                    rank[rooty] +=1 
                return True
            return False

        parent = {}
        for i in range(0,n):
            parent[i] = i

        for i in range(0,n):
            parent[i] = find(i)
        
        rank = [0]*n
        for time, x, y in logs:
            #print(n)
            if union(x,y):
                n -=1
                if n == 1:
                    return time
        return -1 
            

