class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        forward = True
        backward = True
        for i in range(0,len(nums)-1):
            if nums[i+1] < nums[i] :
                forward = False

        nums = nums[::-1]
        for i in range(0,len(nums)-1):
            if nums[i+1] < nums[i] :
                backward = False
        
        return any([forward,backward])