class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        from collections import Counter 
        mapping = Counter(nums)
        highest = max([item[1] for item in mapping.items()])
        values = [item[0] for item in mapping.items() if item[1] == highest]
        counting = 0 
        for i in range(0,len(values)):
            counting += mapping[values[i]]
        return counting  