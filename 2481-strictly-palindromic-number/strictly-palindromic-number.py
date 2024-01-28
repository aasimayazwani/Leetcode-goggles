class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2,n-1):
            if self.check_palindrome(bin(i)[2:]) == True:
                pass 
            else:
                return False 
        return True
        
    def check_palindrome(self,string):
        left = 0 
        right = len(string)-1
        while left <= right:
            if string[left] != string[right]:
                return False 
            else:
                left +=1 
                right -=1 
                pass 
        return True 