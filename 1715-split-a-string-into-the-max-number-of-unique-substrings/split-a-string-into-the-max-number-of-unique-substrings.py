class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        ans = []
        def backtrack(s,combined):
            #print(combined)
            if len(s) == 0:
                ans.append(set(combined))
            if len(s) > 0:
                if len(combined) == 0:
                    backtrack(s[1:],combined + [s[0]])
                else:
                    backtrack(s[1:],combined[0:-1] + [combined[-1] + s[0]])
                    backtrack(s[1:],combined + [s[0]])
        backtrack(s,[])
        return max([len(item) for item in ans])