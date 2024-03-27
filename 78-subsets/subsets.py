class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def back(nums,cur):
            if len(nums) == 0:
                ans.append(sorted(cur))
            else:
                ans.append(cur)
                for i in range(0,len(nums)):
                    back(nums[i+1:],cur+[nums[i]])
        back(nums,[])
        return ans 
