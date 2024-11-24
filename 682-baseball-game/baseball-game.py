class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0
        for i in range(0,len(operations)):
            if operations[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif operations[i] == "C":
                stack.pop(-1)
            elif operations[i] == "D":
                stack.append(stack[-1]*2)
            else:
                stack.append(int(operations[i]))
        return sum(stack)