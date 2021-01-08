class Solution:
    def isPowerOfTwo(self, n) -> bool:
        value =1 
        if n ==1:
            return True 
        if n > 1:
            while value <= n :
                value = value*2 
                if value == n:
                    return True 
        return False 