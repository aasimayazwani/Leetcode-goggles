class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        counting = 0
        for i in range(0,len(nums)):
            if nums[i] != 0:
                nums.append(nums[i])
            else:
                counting +=1 
        for i in range(0,len(nums)):
            if nums[i] == 0:
                nums.append(0)
        del nums[0:length]

        