class Solution:
    def repeatedCharacter(self, s: str) -> str:
        mapping = {}
        for i in range(0,len(s)):
            if s[i] in mapping:
                return s[i]
    
            if s[i] not in mapping:
                mapping[s[i]] = 1 

        