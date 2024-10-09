class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = [0]
        for i in range(0,len(nums)):
            total.append(nums[i]+total[-1])
        return total[1:]