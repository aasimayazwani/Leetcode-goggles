class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s = [item for item in s]
        for i in range(0,len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if s[i] == stack[-1]:
                    stack.pop(-1)
                else:
                    stack.append(s[i])
        return "".join(stack)