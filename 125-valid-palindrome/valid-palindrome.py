class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [item.lower() for item in s if item.isalpha() is True or item.isdigit() is True]
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False 
            else:
                left +=1 
                right -=1 
        return True 
