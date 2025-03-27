class Solution:
    def isHappy(self, n: int) -> bool:
        counter = 0
        while counter < 400:
            n = str(n)
            total = 0
            for i in n:
                total += int(i)*int(i)
            if total == 1:
                return True 
            else:
                n = total
            
            counter +=1 
        return False