class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        for i in range(0,len(grid)):
            heapq.heapify(grid[i])
        ans = 0 
        while col > 0:
            temp = 0
            for j in range(0,row):
                cur = heapq.heappop(grid[j])
                temp = max(cur,temp)
            col -=1
            ans += temp 
        return ans 