class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        from collections import Counter
        import math
        mapping = Counter(nums)

        removable = [item[0] for item in list(mapping.items()) if item[1]%2 ==0]
        counting = 0
        for i in range(0,len(removable)):
            counting += int(mapping[removable[i]]/2)


        left = [item for item in list(mapping.keys()) if item not in removable]
        final = 0
        for item in left:
            counting += int(math.floor(mapping[item]/2))
            final += mapping[item]%2
            
        return [counting,final]