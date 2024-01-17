class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # the position doesn't seem relevant it seems only the presence
        # could check to remove duplicates to begin with 
        # all the nums are <> 0 
        # 
        nums = list(set(nums))
        from collections import Counter
        mapping = Counter(nums) 
        nums = sorted(nums)
        for i in range(0,len(nums)):
            if -nums[-i-1] in mapping:
                return nums[-i-1]
            else:
                pass 
        return -1 