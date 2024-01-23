class Solution:
    def countLetters(self, s: str) -> int:
        from collections import Counter 
        counting = []
        for length in range(1,len(s)):
            current = s[0:length-1]
            for i in range(length-1,len(s)):
                current = current + s[i]
                if len(set(current)) ==1:
                    counting.append(current)
                current = current[1:]
        if len(set(s)) == 1:
            counting.append("1")
        return len(counting)