class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        from collections import Counter 
        nums = sorted(list(set(nums)))
        mapping = Counter(nums)
        explored = {}
        total = 0 
        for i in range(0,len(nums)):
            counting = 0 
            current = nums[i]
             
            while True and (current not in explored):
                explored[current] = 1
                if current in mapping:
                    counting += 1
                    total = max(total,counting)
                    current +=1 
                else:
                    break
            #print(total)
        return total 