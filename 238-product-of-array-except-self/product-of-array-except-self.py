class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = []
        product = 1
        for i in range(0,len(nums)):
            if nums[i] == 0:
                zero_count.append(i)
            else:
                product = product*nums[i]

        if len(zero_count) > 1:
            return [0]*len(nums)
        elif len(zero_count) == 1:
            result = [0]*len(nums)
            result[zero_count[0]] = product
        else:
            result = [product]*len(nums)
            for i in range(0,len(nums)):
                result[i] = int(result[i]/nums[i])
        return result            
            