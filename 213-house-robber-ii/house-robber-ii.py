class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        def recurse(nums,i,dp):
            if i >= len(nums):
                return 0
            else:
                if i not in dp:
                    keep = nums[i] + recurse(nums,i+2,dp)
                    leave = recurse(nums,i+1,dp)
                    dp[i] = max(keep,leave)
                    return dp[i]
                else:
                    return dp[i]

        length = len(nums)
        return max(recurse(nums[0:length-1],0,{}),recurse(nums[1:length],0,{}))