class Solution:
    def numIslands(self, grid: List[List[str]]):
        rows, columns = len(grid), len(grid[0])
        uf = unionfind(grid)

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    for dr, dc in directions:
                        nr = dr + r
                        nc = dc + c
                        if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == "1":
                            uf.union(uf.get_id(r, c, columns), uf.get_id(nr, nc, columns))

        return uf.count 

class unionfind:
    def __init__(self,grid):
        self.parent = {}
        self.rank = {}
        self.count = 0 
        
        rows, columns = len(grid), len(grid[0])
        for i in range(0,rows):
            for j in range(0,columns):
                if grid[i][j] == "1":
                    node_id = self.get_id(i,j,columns)
                    self.parent[node_id] = node_id
                    self.rank[node_id] = 0 
                    self.count +=1 
                    
    def get_id(self,r,c,num_columns):
        return r*num_columns + c
         
    def find(self,node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        
    def union(self,nodex,nodey):
        rootx, rooty = self.find(nodex), self.find(nodey)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
                self.rank[rootx] +=1

            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
                self.rank[rooty] +=1

            elif self.rank[rootx] == self.rank[rooty]:
                self.parent[rooty] = rootx
                self.rank[rootx] +=1 

            self.count -=1 
        
