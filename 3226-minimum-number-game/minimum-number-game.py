class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # remove the minimum element first alice and theb bob 
        # Bob element added, 
        nums = sorted(nums)
    
        result = []

        while len(nums) > 0:
            to_remove = list(reversed(nums[0:2]))
            nums = nums[2:]
            result.extend(to_remove)
        return result 
