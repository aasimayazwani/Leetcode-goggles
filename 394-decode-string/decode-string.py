class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            if s[i]== "]":
                substring = []
                while (stack[-1] != "["):
                    substring.append(stack[-1])
                    stack.pop(-1)
                stack.pop(-1)
                number = ""
                while (len(stack) > 0) and (stack[-1].isdigit() == True):
                    number += stack[-1]
                    stack.pop(-1)
                print(number)
                current = "".join(substring)[::-1]
                current = current*int(number[::-1])
                stack.extend(current)
            else:
                stack.append(s[i])
        return "".join(stack)