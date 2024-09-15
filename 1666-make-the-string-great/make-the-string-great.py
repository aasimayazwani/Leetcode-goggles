class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        s = [item for item in s]
        while len(s) > 0 :
            if len(stack) == 0:
                stack.append(s[0])
                s.pop(0)
            else:
                if (s[0].lower() == stack[-1].lower()) and ((s[0].isupper() and stack[-1].islower()) or (s[0].islower() and stack[-1].isupper())):
                    stack.pop(-1)
                    s.pop(0)
                else:
                    stack.append(s[0])
                    s.pop(0)
                
        return "".join(stack)