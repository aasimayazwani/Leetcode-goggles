class Solution:
    def removeDuplicates(self, nums):
        number = 1
        if len(nums) <2:
            return 1
        else:
            while number != 0:
                nums = self.removing(nums)
                number = self.repeats(nums)
            return len(nums) 
    
    def removing(self,nums):
        slower = 0 
        faster = 1 
        while faster < len(nums):
            if nums[faster] == nums[slower]:
                del nums[slower]
            slower +=1
            faster +=1
        return nums
    
    def repeats(self,nums):
        counts = [] 
        slower = 0 
        faster = 1  
        while faster < len(nums):
            if nums[faster] == nums[slower]:
                counts.append(slower)
            slower +=1
            faster +=1
        return len(counts)