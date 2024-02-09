class Solution:
    def maxDepth(self, s: str) -> int:
        max_stack = 0
        stack = []
        for i in range(0,len(s)):
            if s[i] == "(":
                stack.append(s[i])
            if s[i] == ")":
                max_stack = max(max_stack,len(stack))
                stack.pop(-1)
        return max_stack