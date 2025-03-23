class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}

        def recurse(i):
            # botton -> top 
            # base condition
            if i >=len(nums):
                return 0 
            else:
                if i in dp:
                    return dp[i]
                else:
                    steal = nums[i] + recurse(i+2)
                    left = recurse(i+1)
                    dp[i] = max(steal,left)
                    return dp[i]
        
        return recurse(0)