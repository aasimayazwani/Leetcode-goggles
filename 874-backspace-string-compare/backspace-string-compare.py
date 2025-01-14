class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.remove(s) == self.remove(t)

    def remove(self,s):
        s = [item for item in s]
        stack = []
        while len(s) > 0:
            if len(stack) == 0:
                if s[0] != "#":
                    stack.append(s.pop(0))
                else:
                    s.pop(0)
            else:
                if s[0] == "#":
                    stack.pop(-1)
                    s.pop(0)
                else:
                    stack.append(s.pop(0))
        return "".join(stack)