class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # logic
        # The questions is only asking if the string entries present 
        # in the ranson note are less then or equal to the magazine. 
        # THe order is not relevant
        # so I will use a dictionary for both the magazine and ransomnote. 
        from collections import Counter 
        c1, c2 = Counter(ransomNote), Counter(magazine)
        keys = list(c1.keys())
        for i in range(0,len(keys)):
            if c1[keys[i]] > c2[keys[i]]:
                return False
        return True 