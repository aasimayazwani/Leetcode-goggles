class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(0,len(s)):
            #print(stack)
            if len(stack) == 0:
                stack.append(s[i])
            else:
                if stack[-1] == s[i]:
                    stack.pop(-1)
                else:
                    stack.append(s[i])
        return "".join(stack)