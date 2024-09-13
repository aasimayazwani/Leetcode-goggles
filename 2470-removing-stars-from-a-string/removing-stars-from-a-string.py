class Solution:
    def removeStars(self, s: str) -> str:
        if len(s) == 1:
            return s 
        stack = []
        while len(s) > 0:
            if len(stack) == 0:
                stack.append(s[0])
                s = s[1:]
            if len(stack) > 0:
                if s[0] == "*":
                    stack.pop(-1)
                    s = s[1:]
                else:
                    stack.append(s[0])
                    s = s[1:]
        return "".join(stack)