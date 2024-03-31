class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        for i in range(0,len(s)):
            #print(stack)
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if ((stack[-1].islower() == s[i].isupper()) or (stack[-1].isupper() == s[i].islower())) and (stack[-1].lower() == s[i].lower()):
                    stack.pop(-1)
                else:
                    stack.append(s[i])
        return "".join(stack)