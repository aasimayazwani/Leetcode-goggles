class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, len(nums)-1
        for left in range(0,len(nums)):
            if nums[left] == 0:
                for right in range(left+1,len(nums)):
                    if nums[right] != 0:
                        nums[left], nums[right] = nums[right], nums[left]
                        break
        return nums 