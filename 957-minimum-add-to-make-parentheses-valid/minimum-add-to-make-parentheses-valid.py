class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        string = [item for item in s]
        return self.checks(s)
        
    def checks(self,string):
        counting = 0
        stack = []
        for i in range(0,len(string)):
            if len(stack) == 0:
                stack.append(string[i])
            else:
                if string[i] == ")":
                    if stack[-1] == "(":
                        stack.pop(-1)
                    else:
                        counting +=1

                if string[i] == "(":
                    stack.append(string[i])

        return counting + len(stack)
            