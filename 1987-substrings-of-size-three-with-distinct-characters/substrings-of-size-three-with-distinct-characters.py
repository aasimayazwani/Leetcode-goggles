class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        counting = 0
        current_string = s[0:2]
        for i in range(2,len(s)):
            current_string += s[i]
            if len(set(current_string)) == 3:
                counting +=1 
            else:
                pass
            current_string = current_string[1:]
        return counting