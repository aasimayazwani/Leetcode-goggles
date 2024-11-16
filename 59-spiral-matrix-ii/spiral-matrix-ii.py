class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[1]*n for i in range(n)]
        window = 0
        counting = 1
        while counting <= n*n:
            if counting <= n*n:
                for r1 in range(window,n-window):
                    grid[window][r1] = counting 
                    counting +=1
            if counting <= n*n:
                for c1 in range(window+1,n-window):
                    grid[c1][n-1-window] = counting
                    counting +=1
            if counting <= n*n:
                for r2 in list(reversed(range(window,n-1-window))):
                    grid[n-window-1][r2] = counting
                    counting +=1
            if counting <= n*n:
                for c2 in list(reversed(range(window+1,n-1-window))):
                    grid[c2][window] = counting
                    counting +=1 
            window +=1 
        return grid 