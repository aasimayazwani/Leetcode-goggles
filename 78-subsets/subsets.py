class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recurse(arr,nums,n):
            if len(arr) < n:
                ans.append(arr)
            elif len(arr) == n:
                ans.append(arr)
                return

            for i in range(0,len(nums)):
                if len(arr) > 0:
                    if arr[-1] < nums[i]:
                        recurse(arr+[nums[i]],nums,n)
                else:
                    recurse(arr+[nums[i]],nums,n)
        ans = []
        recurse([],nums,len(nums))
        return ans 
            