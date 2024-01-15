class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # the question is asking us to preserve the dictionary of s and t
        from collections import Counter
        s_dict = Counter(s)
        t_dict = Counter(t)
        if s_dict == t_dict:
            return True 
        return False