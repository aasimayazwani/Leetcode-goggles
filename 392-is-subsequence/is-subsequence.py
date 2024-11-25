class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = [item for item in s]
        t = [item for item in t]
        t_pointer = 0
        if len(s) == 0:
            return True
        
        while t_pointer < len(t):
            if t[t_pointer] == s[0]:
                s.pop(0)
                t_pointer +=1 
                if len(s) == 0:
                    return True
            else:
                t_pointer +=1 
        return False 
