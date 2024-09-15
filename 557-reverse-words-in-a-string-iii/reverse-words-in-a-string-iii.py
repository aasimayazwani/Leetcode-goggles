class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        s = s.split(" ")
        for i in range(0,len(s)):
            answer.append(self.reverse([item for item in s[i]]))
        return " ".join(answer)

    def reverse(self,s):
        left, right = 0,len(s)-1
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left +=1 
            right -=1 
        return "".join(s)