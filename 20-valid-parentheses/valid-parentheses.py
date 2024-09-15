class Solution:
    def isValid(self, s: str) -> bool:
        left = ["[","(","{"]
        right = ["]",")","}"]
        s = [item for item in s]
        mapping = {}
        for i in range(0,len(left)):
            mapping[left[i]] = right[i]
        stack = []
        while len(s) > 0:
            if len(stack) == 0:
                stack.append(s[0])
                s.pop(0)
            else:
                if s[0] in mapping:
                    stack.append(s[0])
                    s.pop(0)
                else :
                    if stack[-1] in mapping:
                        if mapping[stack[-1]] == s[0]:
                            stack.pop(-1)
                            s.pop(0)
                        else:
                            return False
                    else:
                        return False
        if len(stack) == 0:
            return True
        return False
                
