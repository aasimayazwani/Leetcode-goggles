class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def recurse(i):
            if i >= len(nums):
                return 0 
            else:
                if i in dp:
                    return dp[i]
                else:
                    keep = nums[i] + recurse(i+2)
                    skipping = recurse(i+1)
                    dp[i] = max(keep,skipping)
                    return dp[i]

        return recurse(0)
