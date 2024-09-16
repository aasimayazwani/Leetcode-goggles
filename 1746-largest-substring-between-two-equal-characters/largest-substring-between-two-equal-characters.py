class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mapping = {}
        for i in range(0,len(s)):
            if s[i] not in mapping:
                mapping[s[i]] = [i]
            else:
                mapping[s[i]].append(i)
        ans = [max(item)-min(item) for item in mapping.values() if len(item) > 1]
        if len(ans) > 0:
            return max(ans) -1 
        return -1 