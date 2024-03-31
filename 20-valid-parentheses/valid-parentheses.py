class Solution:
    def isValid(self, s: str) -> bool:
        closing =  ["}",")","]"]
        stack = []
        for i in range(0,len(s)):
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if s[i] in closing:
                    if (s[i] == ")" and stack[-1] == "(") or (s[i] == "}" and stack[-1] == "{") or (s[i] == "]" and stack[-1] == "["):
                        stack.pop(-1)
                    else:
                        return False
                else:
                    stack.append(s[i])
        if len(stack) > 0:
            return False 
        return True