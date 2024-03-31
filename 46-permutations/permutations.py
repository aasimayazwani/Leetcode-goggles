class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # all integers are distinct, so no need to worry about duplicates
        ans = []
        def back(nums,current):
            if len(nums) == 0:
                ans.append(current)
            if len(nums) > 0:
                for i in range(0,len(nums)):
                    back(nums[0:i] + nums[i+1:], current+[nums[i]])
            else:
                return 

        back(nums,[])
        return ans 
        