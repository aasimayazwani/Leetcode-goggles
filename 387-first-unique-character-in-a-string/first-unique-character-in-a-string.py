class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapping = {}
        for i in range(0,len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = [i]
            else:
                mapping[s[i]].append(i)
        
        ans = [item[1][0] for item in mapping.items() if len(item[1])==1]
        if len(ans) > 0:
            return min(ans)
        return -1 
        