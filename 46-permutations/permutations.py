class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def recurse(arr,nums):
            if len(arr) == len(nums):
                ans.append(arr)
                return 
            for i in range(0,len(nums)):
                if nums[i] not in arr:
                    recurse(arr+[nums[i]],nums)
                else:
                    pass
        recurse([],nums)
        return ans 
        
            