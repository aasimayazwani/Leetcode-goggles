class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(0,len(s)):
            #print(stack)
            if (len(stack)>0) and ((stack[-1] == "[" and s[i] == "]") or (stack[-1] == "{" and s[i] == "}") or (stack[-1] == "(" and s[i] == ")")):
                stack.pop(-1)
            else:
                stack.append(s[i])
                
        return len(stack) == 0