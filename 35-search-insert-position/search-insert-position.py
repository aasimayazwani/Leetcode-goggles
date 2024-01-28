class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        arr = nums 
        left = 0 
        right = len(arr) - 1
        while left <= right:
            middle = left + (right - left)//2 
            if arr[middle] == target:
                return middle
            if arr[middle] > target:
                right = middle - 1 
            if arr[middle] < target:
                left = middle + 1
        return left