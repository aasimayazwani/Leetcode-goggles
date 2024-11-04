class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        positive, negative = [], []
        parent= {}
        for i in range(0,len(equations)):
            cur = equations[i]
            parent[cur[0]] = cur[0]
            parent[cur[-1]] = cur[-1]
            if cur[1] == "=":
                positive.append([cur[0],cur[-1]])
            else:
                negative.append([cur[0],cur[-1]])
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(nodex, nodey):
            nodex, nodey = find(nodex), find(nodey)
            if nodex != nodey:
                parent[nodey] = nodex
    
        for i in range(0,len(positive)):
            x,y = positive[i]
            union(x,y)
            
        for i in range(0,len(negative)):
            x,y = negative[i]
            if find(x) == find(y):
                return False
        return True 