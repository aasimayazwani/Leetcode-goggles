class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0 
        t_pointer = 0 
        result = []
        # keep the s_pointer in place until a match is found 
        while (s_pointer < len(s)) and (t_pointer < len(t)):
            if s[s_pointer] == t[t_pointer]:
                result.append(t_pointer)
                s_pointer +=1
                t_pointer +=1
            else  :
                t_pointer +=1

        return len(result) == len(s)
 