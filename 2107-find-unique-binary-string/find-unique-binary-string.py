class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        candidates = ["0","1"]
        result = []
        def backtrack(nums,current,length,original):
            if (len(current) == length):
                if (current not in original):
                    result.append(current)
            if len(current) < length:
                for i in range(0,len(nums)):
                    backtrack(nums,current + nums[i],length,original)
            if len(current) > length:
                return 
        backtrack(candidates,"",length,nums)
        #print(result)
        return [item for item in result if item not in nums][0]
