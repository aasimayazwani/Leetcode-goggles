class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        nums = sorted(nums)
        maximum = -1
        while left < right:
            current_pair = [nums[left],nums[right]]
            left +=1 
            right -=1
            total = sum(current_pair)
            maximum = max(maximum,total)
        
        return maximum 
            