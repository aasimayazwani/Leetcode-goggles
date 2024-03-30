class Solution:
    def minLength(self, s: str) -> int:
        if len(s) < 2:
            return 1 
        stack = []
        for i in range(0,len(s)):
            if (len(stack) > 0) and ((s[i] == "B" and stack[-1] =="A") or (s[i] == "D" and stack[-1] =="C")):
                stack.pop(-1)
            else:
                stack.append(s[i])
        return len(stack)
