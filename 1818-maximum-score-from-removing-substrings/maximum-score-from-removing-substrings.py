class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x > y:
            s1, score1 = self.increment(s,"a","b",0,x)
            s2, score2 = self.increment(s1,"b","a",score1,y)
            return score2
        else:
            s1, score1 = self.increment(s,"b","a",0,y)
            s, score2 = self.increment(s1,"a","b",score1,x)
            return score2

    def increment(self,s,chr1,chr2,score,increment_val):
        stack = []
        for i in range(0,len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if stack[-1] == chr1 and s[i] == chr2:
                    score += increment_val
                    stack.pop(-1)
                else:
                    stack.append(s[i])
        return "".join(stack), score 