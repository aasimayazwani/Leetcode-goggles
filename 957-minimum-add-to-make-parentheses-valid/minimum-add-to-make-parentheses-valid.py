class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        error_count = 0
        s = [item for item in s]
        for i in range(0,len(s)):
            if len(stack) == 0:
                if s[i] == "(":
                    stack.append(s[i])
                else:
                    error_count +=1
            else:
                if s[i]  == "(":
                    stack.append(s[i])
                else :
                    if stack[-1] == "(":
                        stack.pop(-1)
                    else:
                        error_count +=1
        return len(stack) + error_count
                
