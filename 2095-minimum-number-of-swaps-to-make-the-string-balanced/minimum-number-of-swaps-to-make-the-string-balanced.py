class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        counting = 0
        for i in range(0,len(s)):
            if len(stack) == 0:
                if s[i] == "[":
                    stack.append(s[i])
                else:
                    stack.append("[")
                    counting +=1 
            else:
                if s[i] == "[":
                    stack.append("[")
                else:
                    if stack[-1] == "[":
                        stack.pop(-1)
                    else:
                        counting +=1 
                        stack.pop(-1)
        return counting 