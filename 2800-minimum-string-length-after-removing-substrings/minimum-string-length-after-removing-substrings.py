class Solution:
    def minLength(self, s: str) -> int:
        stack, s = [], [item for item in s]
        for i in range(0,len(s)):
            if s[i] == "B":
                if len(stack) > 0 and stack[-1] == "A":
                    stack.pop(-1)
                else:
                    stack.append(s[i])
            elif s[i] == "D":
                if len(stack) > 0 and stack[-1] == "C":
                    stack.pop(-1)
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        return len(stack)
                    