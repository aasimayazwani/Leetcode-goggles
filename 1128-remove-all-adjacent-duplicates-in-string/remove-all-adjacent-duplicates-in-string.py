class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        s = [item for item in s]
        while len(s) > 0 :
            if len(stack) == 0:
                stack.append(s.pop(0))
            else:
                if s[0] == stack[-1]:
                    stack.pop(-1)
                    s.pop(0)
                else:
                    stack.append(s.pop(0))
        return "".join(stack)