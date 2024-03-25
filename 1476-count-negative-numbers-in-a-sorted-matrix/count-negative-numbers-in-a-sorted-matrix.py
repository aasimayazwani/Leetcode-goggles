class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        counting = 0
        for i in range(0,len(grid)):
            counting += self.bs(grid[i][::-1])
        return counting 

    def bs(self,arr):
        left = 0 
        right = len(arr) - 1
        target = 0
        while left <= right:
            middle = left + (right - left)//2
            if arr[middle] >= target:
                right = middle - 1
            if arr[middle] < target:
                left = middle + 1 
            #if arr[middle] == target:
            #    return middle
        return left

