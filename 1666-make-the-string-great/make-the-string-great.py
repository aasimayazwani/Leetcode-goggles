class Solution:
    def makeGood(self, s: str) -> str:
        s = [item for item in s ]
        stack = []
        while s:
            if len(stack) == 0:
                stack.append(s.pop(0))
            else:
                if stack[-1].lower() == s[0].lower():
                    if (stack[-1].isupper() and s[0].islower()) or (stack[-1].islower() and s[0].isupper()):
                        stack.pop(-1)
                        s.pop(0)
                    else:
                        stack.append(s.pop(0))
                else:
                    stack.append(s.pop(0))
        return "".join(stack) 