class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = {}
        for i in range(0,len(grid)):
            rows[i+1] = max(grid[i])

        columns = {}
        for i in range(0,len(grid)):
            values = []
            for j in range(0,len(grid)):
                values.append(grid[j][i])
            columns[i+1] = max(values)

        counting = 0
        for i in range(0,len(grid)):
            ans = []
            for j in range(0,len(grid)):
                counting += min(rows[i+1],columns[j+1]) - grid[i][j]
                #print(max(grid[i][j],rows[i+1],columns[j+1]))

        return counting 
