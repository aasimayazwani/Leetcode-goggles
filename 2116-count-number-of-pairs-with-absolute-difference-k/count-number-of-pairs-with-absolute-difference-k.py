class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        from collections import Counter
        mapping = Counter(nums)
        keys = list(mapping.keys())
        counting = 0
        for i in range(0,len(keys)):
            if keys[i] + k  in mapping:
                counting += mapping[keys[i] + k]*mapping[keys[i]]
            if keys[i] - k  in mapping:
                counting += mapping[keys[i] - k]*mapping[keys[i]]
        return int(counting/2)