class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(nums,cur):
            if len(nums)==0:
                ans.append(cur)
            else:
                for i in range(0,len(nums)):
                    backtrack(nums[0:i]+nums[i+1:], cur+[nums[i]])
        backtrack(nums,[])
        return ans