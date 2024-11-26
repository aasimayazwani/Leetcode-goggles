class Solution:
    def isHappy(self, n: int) -> bool:
        iterations = 0 
        while iterations < 100:
            iterations +=1
            n = [int(item) for item in str(n)]
            total = 0
            for i in range(0,len(n)):
                total += n[i]**2
            if total == 1:
                return True
            n = str(total)
        if int(n) != 100:
            return False
        return True 