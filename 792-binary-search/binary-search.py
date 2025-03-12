class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0 , len(nums)-1
        if target < nums[0] or target > nums[-1]:
            return -1
        while left <= right:
            mid = left+(right-left)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1 