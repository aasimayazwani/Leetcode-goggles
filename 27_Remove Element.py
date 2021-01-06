class Solution:
    def removeElement(self, nums, val):
        iterations = 0 
        while iterations <= len(nums):
            nums = self.removing(nums,val)
            iterations +=1
            #print(nums)
        return len(nums)

    def removing(self,nums,target):
        slower = 0 
        while slower < len(nums):
            if nums[slower]==target:
                del nums[slower]
            slower +=1
        return nums