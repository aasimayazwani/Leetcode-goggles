class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1 
        while left <= right:
            middle = left + (right-left)//2
            mid = nums[middle]
            if target == mid:
                return middle
            if target > mid:
                left = middle + 1
            if target < mid:
                right = middle - 1
        return -1  
            
