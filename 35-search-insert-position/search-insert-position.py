class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid -1 
        return left
    