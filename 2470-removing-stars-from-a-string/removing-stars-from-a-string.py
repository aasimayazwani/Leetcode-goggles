class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            if s[i] != "*":
                stack.append(s[i])
            else:
                stack.pop(-1)
        if len(stack) == 0:
            return ""
        return "".join(stack)
