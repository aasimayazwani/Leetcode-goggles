class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(0,length):
            if i == 0:
                nums.append(nums[i])
            else:
                if nums[i] != nums[-1]:
                    nums.append(nums[i])
                else:
                    pass 
        del nums[0:length]
        return len(nums)
        
        