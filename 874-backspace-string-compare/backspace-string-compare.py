class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.operate(s) == self.operate(t)

    def operate(self,string):
        stack = []
        string = [item for item in string]
        for i in range(0,len(string)):
            if len(stack) == 0:
                if string[i] != "#":
                    stack.append(string[i])
                else :
                    pass
            else:
                if string[i] == "#":
                    stack.pop(-1)
                else:
                    stack.append(string[i])
        return "".join(stack)