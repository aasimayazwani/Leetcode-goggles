class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        r, c = len(grid), len(grid[0])
        directions = [(0,1),(1,0)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    perimeter +=4 
                    for dx, dy in directions:
                        nx, ny = i + dx, j+dy
                        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 1:
                            perimeter -= 2 
                #print(perimeter)
        return perimeter 
                