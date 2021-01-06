class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        summation = 0 
        for i in range(0,len(nums)):
            summation+=nums[i]
            res.append(summation)
        return res 