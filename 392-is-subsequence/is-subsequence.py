class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = [item for item in s]
        t = [item for item in t]
        # if the first element of t matches the first element of s, 
        # delete these elements, but if they don't match pop the first element of t 
        # keep on doing this until matches are found 
        # stop the process when either the s or t have length of zero. 
        while (len(s) != 0) and (len(t) != 0):
            if s[0] == t[0]:
                s.pop(0)
                t.pop(0)
            elif s[0] != t[0]:
                t.pop(0)
        return len(s) == 0 