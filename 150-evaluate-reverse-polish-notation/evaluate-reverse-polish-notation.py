class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        tokens = [item for item in tokens]
        mapping = {"+":1,"-":1,"*":1,"/":1}
        stack = []
        while len(tokens) > 0:
            #print(stack)
            if len(stack) < 2:
                stack.append(tokens[0])
                tokens.pop(0)
            else :
                if tokens[0] in mapping:
                    operation = stack[-2] + tokens[0] + stack[-1]
                    tokens.pop(0)
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(str(int(eval(operation))))
                else:
                    stack.append(str(tokens[0]))
                    tokens.pop(0)
        return int(stack[0])