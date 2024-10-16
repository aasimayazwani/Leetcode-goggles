class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, result = [], [0]*len(temperatures)
        for i in range(0,len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                result[stack[-1]] = abs(i-stack[-1])
                stack.pop(-1)
            stack.append(i)
        return result