class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            if (len(stack) > 0) and (s[i] =="*"):
                stack.pop(-1)
            else:
                stack.append(s[i])
        return "".join(stack)
        