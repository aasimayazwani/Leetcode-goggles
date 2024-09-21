class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        left, right = 0,len(nums)-1
        averages = 100000
        while left < right:
            current = (nums[left]+nums[right])/2
            left +=1 
            right -=1
            averages = min(averages,current)
        return averages