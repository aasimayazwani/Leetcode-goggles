class Solution:
    def clearDigits(self, s: str) -> str:
        s = [item for item in s]
        stack = []
        while len(s) > 0:
            if s[0].isdigit():
                if len(stack) > 0:
                    stack.pop(-1)
                    s.pop(0)
                else:
                    s.pop(0)
                    pass
            else:
                stack.append(s[0])
                s.pop(0)
        return ''.join(stack)