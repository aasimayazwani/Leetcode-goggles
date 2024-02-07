class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            print(stack)
            if s[i] == ")":
                substring = []
                while stack[-1] != "(":
                    substring.append(stack[-1])
                    stack.pop(-1)
                stack.pop(-1)
                stack.extend(substring[0:])
            else:
                stack.append(s[i])
        return "".join(stack)        