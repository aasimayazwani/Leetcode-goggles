class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mapping = {"+":1,"-":1,"*":1,"/":1}
        stack = []
        for i in range(0,len(tokens)):
            if len(stack) <2:
                stack.append(tokens[i])
            else:
                #print(stack)
                if tokens[i] in mapping:
                    operation = stack[-2] + tokens[i] + stack[-1]
                    value = int(eval(operation))
                    stack.pop(-1)
                    stack.pop(-1)
                    stack.append(str(value))
                else:
                    stack.append(tokens[i])
        
        return int(stack[0])