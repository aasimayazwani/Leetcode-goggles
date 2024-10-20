class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left, right = 0, 1
        for left in range(0,len(nums)):
            #print(nums)
            if nums[left] == 0:
                for right in range(left, len(nums)):
                    if nums[right] != 0:
                        nums[left], nums[right] = nums[right], nums[left]
                        break
            else:
                pass
        