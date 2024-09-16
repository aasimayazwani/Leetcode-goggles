class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = [item for item in s]
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left].isalpha() and s[right].isalpha():
                s[left], s[right] = s[right], s[left]
                left +=1 
                right -=1 
            else:
                if s[left].isalpha() and s[right].isalpha() == False:
                    right -=1 
                if s[left].isalpha() == False and s[right].isalpha():
                    left +=1 
                if s[left].isalpha() == False and s[right].isalpha() == False:
                    left +=1 
                    right -=1
        return "".join(s)