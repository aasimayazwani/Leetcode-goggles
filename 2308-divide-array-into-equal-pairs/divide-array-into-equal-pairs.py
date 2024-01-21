class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        from collections import Counter
        mapping = Counter(nums)
        nums = list(set(nums))
        for i in range(0,len(nums)):
            if mapping[nums[i]]%2 == 0:
                pass 
            else:
                return False

        return True 