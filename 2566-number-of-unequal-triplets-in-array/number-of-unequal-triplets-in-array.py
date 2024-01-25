class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        result = 0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        result +=1 

        
        return result 
        #return len(Counter(result).keys())