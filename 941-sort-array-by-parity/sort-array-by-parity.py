class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1 
        while left < right:
            if nums[left]%2 is not 0 and nums[right]%2 is 0:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1 
                right -=1
            elif nums[left]%2 is 0 and nums[right]%2 is not 0:
                left +=1 
                right -=1
            elif nums[left]%2 is 0 and nums[right]%2 is 0:
                left +=1 
            elif nums[left]%2 is not 0 and nums[right]%2 is not 0:            
                right -=1 
        return nums 
        