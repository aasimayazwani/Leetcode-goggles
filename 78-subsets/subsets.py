class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(nums,current):
            if len(nums) == 0:
                ans.append(current)
            if len(nums) > 0:
                ans.append(current)
                for i in range(0,len(nums)):
                    backtrack(nums[i+1:],current+[nums[i]])
        backtrack(nums,[])
        return ans 