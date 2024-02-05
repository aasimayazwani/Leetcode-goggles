class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        for i in range(0,length):
            if nums[i] != val:
                nums.append(nums[i])
            else:
                pass 
        del nums[0:length]
        return len(nums)

             