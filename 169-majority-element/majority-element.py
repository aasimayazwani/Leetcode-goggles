class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use a hashmap to keep track of the frequency of elemtns 
        # then use hashmpa items to search for items which occur greater then n/2 
        # the moment you find them stop, searching since only 
        # one element can occure n/2 times. 
        import math
        length = math.ceil(len(nums)/2)
        mapping = {}
        for i in range(0,len(nums)):
            if nums[i] in mapping:
                mapping[nums[i]] +=1 
            if nums[i] not in mapping:
                mapping[nums[i]] = 1
        pairs = list(mapping.items())
        for key, value in pairs:
            if value >= length:
                return key
