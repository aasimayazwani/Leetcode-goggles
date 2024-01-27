class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        result = [] 
        for i in range(0,len(l)):
            arr = nums[l[i]:r[i]+1]
            print(arr)
            result.append(self.check(arr))
        return result 

    def check(self,nums):
        nums = sorted(nums)
        if len(nums) < 2:
            return False 
        else:
            difference = nums[1] - nums[0]
            for i in range(0,len(nums)-1):
                if nums[i+1] - nums[i] != difference:
                    return False 
                else:
                    pass 
            return True 
                