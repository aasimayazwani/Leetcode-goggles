class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = [item for item in s ]
        ans = ""
        counter = 0
        for i in range(0,len(s),k):
            cur = s[i:i+k]
            if counter%2 == 0:
                ans += self.rev(cur)
            else:
                ans += "".join(cur)
            counter +=1 
        return ans 
    
    
    def rev(self,s):
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1 
            right -=1 
        return "".join(s)
    