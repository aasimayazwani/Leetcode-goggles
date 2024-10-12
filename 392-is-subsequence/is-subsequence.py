class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = [item for item in s]
        t = [item for item in t]
        if len(s) == 0 :
            return True 
        for i in range(0,len(t)):
            if t[i] == s[0]:
                s.pop(0)
            if len(s) == 0:
                return True
        return len(s) == 0 