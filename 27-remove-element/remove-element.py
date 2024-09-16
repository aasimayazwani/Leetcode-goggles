class Solution:
    def removeElement(self, nums, val):
        if len(nums) == 0:
            return 0 
        else:
            k = 0
            right = len(nums)-1
            for left in range(0,len(nums)):
                if nums[left] == val:
                    status = True
                    while (status) and (left < right):
                        if nums[right] == val:
                            right -=1
                        if nums[right] != val:
                            nums[left],nums[right] = nums[right], nums[left]
                            right -=1 
                            status = False
                if nums[left] != val:
                    k += 1
            return k