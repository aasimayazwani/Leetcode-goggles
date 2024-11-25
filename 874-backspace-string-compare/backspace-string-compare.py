class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        a = self.convert(s)
        b = self.convert(t)
        print(a)
        print(b)
        return a == b 

        
    def convert(self,s):
        s = [item for item in s ]
        stack = []
        while s :
            if len(stack) == 0:
                if s[0] != "#":
                    stack.append(s.pop(0))
                else:
                    s.pop(0)
            else:
                if s[0] == "#":
                    if len(stack) > 0:
                        stack.pop(-1)
                        s.pop(0)
                    
                else:
                    stack.append(s.pop(0))
        return "".join(stack)                