class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        while len(s) > 0 and len(t) > 0:
            if s[0] == t[0]:
                s.pop(0)
                t.pop(0)
            else:
                return t[0]
        return t[0]