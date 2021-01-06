class Solution:
    def firstMissingPositive(self, nums):
        nums = set(nums)
        curr = 1
        while 1:
            if not (curr in nums):
                return curr
            curr += 1