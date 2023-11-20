class Solution:
    def findContestMatch(self, n: int) -> str:
        
        def formGroup(p1, p2, res):
            if p1 >= p2:
                return res
            
            temp = []
            while p1 < p2:
                temp.append((res[p1],res[p2]))
                p1 += 1
                p2 -= 1
                
            p1 = 0
            p2 = len(temp)-1
            res = temp[:]
            
            return formGroup(p1, p2, res)
            
        res = list(range(1, n+1))
        
        res = formGroup(0, n-1, res)
        res = str(res[0])
        ans = ""
        
        for i in res:
            if i == " ":
                continue
            ans += i
        
        return ans
        
            
            