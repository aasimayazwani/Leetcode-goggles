class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # i != j 
        # sum of digits of i= 
        values = [sum([int(item) for item in str(item)]) for item in nums]
        mapping = {}
        for i in range(0,len(nums)):
            if values[i] in mapping:
                mapping[values[i]].append(nums[i])
            if values[i] not in mapping:
                mapping[values[i]] = [nums[i]]


        result =  [sum(sorted(item[1],reverse=True)[0:2]) for item in mapping.items() if len(item[1])>1]
        
        if len(result) > 0:
            return max(result)
        else:
            return -1 