class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(current,nums):
            if len(current)==len(nums):
                ans.append(current)
            elif len(current) < len(nums):
                for i in range(0,len(nums)):
                    if nums[i] not in current:
                        backtrack(current+[nums[i]],nums)
        backtrack([],nums)
        return list(set([tuple(item) for item in ans]))