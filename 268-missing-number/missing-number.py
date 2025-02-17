class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)
        while left < right:
            print(nums[left:right+1])
            mid = left + (right-left)//2
            if nums[mid] > mid:
                right = mid
            elif nums[mid] == mid:
                left = mid + 1
        return right