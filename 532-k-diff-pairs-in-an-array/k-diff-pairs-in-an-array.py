class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter
        mapping = Counter(nums)
        counting = 0 
        
        keys = list(mapping.keys())
        counting = 0
        for i in range(0,len(keys)):
            if k > 0 and keys[i] - k  in mapping:
                counting += 1
            elif (k == 0) and (mapping[keys[i]] > 1):
                counting +=1 

        return counting