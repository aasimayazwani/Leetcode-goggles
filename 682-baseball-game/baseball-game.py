class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        ops = operations
        while len(ops):
            cur = ops[0]
            if cur == "+":
                total = int(stack[-1]) + int(stack[-2])
                stack.append(total)
                ops.pop(0)
            elif cur == "D":
                stack.append(2*int(stack[-1]))
                ops.pop(0)
            elif cur == "C":
                stack.pop(-1)
                ops.pop(0)
            else:
                stack.append(int(cur))
                ops.pop(0)
        print(stack)
        return sum(stack)