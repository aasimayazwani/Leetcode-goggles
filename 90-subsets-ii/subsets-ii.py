class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def iterate(arr,nums):
            if len(nums) == 0:
                if arr not in ans:
                    ans.append(arr)
            else:
                if arr not in ans:
                    ans.append(arr)
                for i in range(0,len(nums)):
                    if len(arr) == 0:
                        iterate(arr + [nums[i]],nums[i+1:])
                    elif arr[-1] <= nums[i]:
                        iterate(arr + [nums[i]],nums[i+1:])
        #nums = [1,2,2]
        nums = sorted(nums)
        iterate([],nums)
        return ans