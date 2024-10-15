class Solution:
    def arraySign(self, nums: List[int]) -> int:
        status = 0
        for i in range(0,len(nums)):
            if nums[i] < 1:
                status +=1
            if nums[i] == 0:
                return 0
            if nums[i] > 1:
                pass
        if status % 2 == 0:
            return 1
        return -1