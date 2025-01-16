class Solution:
    def isValid(self, s: str) -> bool:
        right = {")":"(","}":"{","]":"["}
        stack = []
        s = [item for item in s]
        while len(s) > 0:
            if len(stack) == 0:
                if s[0] in right:
                    return False 
                else:
                    stack.append(s.pop(0))
            else:
                if s[0] not in right:
                    stack.append(s.pop(0))
                else:
                    if right[s[0]] == stack[-1]:
                        stack.pop(-1)
                        s.pop(0)
                    else:
                        return False 
        if len(s) == 0 and len(stack) == 0:
            return True 
        return False 

