class Solution:
    def beautySum(self, s: str) -> int:
        from collections import Counter
        counting = 0 
        for size in range(2,len(s)):
        #size = 2
            current = s[0:size]
            for i in range(size,len(s)):
                current = current + s[i]
                #print(current)
                counting += self.get_beauty(current)
                current = current[1:]
        return counting 


    def get_beauty(self,s):
        mapping = Counter(s)
        values = [item[1] for item in list(mapping.items())]
        c =  max(values) - min(values)
        return c