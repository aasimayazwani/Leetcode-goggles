class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        stack = []
        s = [item for item in s]
        for i in range(0,len(s)):
            if s[i]  == "(":
                stack.append(s[i])
            elif s[i] == ")":
                max_depth = max(max_depth,len(stack))
                stack.pop(-1)
        return max_depth