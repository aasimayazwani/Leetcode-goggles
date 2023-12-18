class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) -1 
        nums = sorted(nums)
        count = 0
        iteration = 0
        while left < right:
            # if the right most element is larger then target 
            # then reduce the right by 1 
            # if the left most element is smaller then 
            # it means all the elements to the left also must be smaller as well. 
            # count += left
            if nums[left] + nums[right] >= target:
                right -=1 
            else:
                count += right - left   
                left +=1 
        return count 

