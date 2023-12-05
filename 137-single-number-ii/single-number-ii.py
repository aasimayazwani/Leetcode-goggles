class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapping = {}
        for i in range(0,len(nums)):
            if nums[i] in mapping:
                mapping[nums[i]] += 1 
            if nums[i] not in mapping:
                mapping[nums[i]] = 1 

        #print(list(mapping.items()))
        return [item[0] for item in list(mapping.items()) if item[1] == 1 ][0]