class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(current,nums):
            #print(current)
            if 0 == len(nums):
                ans.append(current)
                return 
            else:
                ans.append(current)
                for i in range(0,len(nums)):
                    backtrack(current + [nums[i]] ,nums[i+1:])
        backtrack([],nums)
        print(ans)
        return ans
            
                