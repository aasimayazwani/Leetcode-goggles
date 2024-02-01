class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x:x[0])
        stack = []
        for i in range(0,len(intervals)):
            if len(stack) < 1:
                stack.append(intervals[i])
            if len(stack)>=1:
                if stack[-1][1] >= intervals[i][0]:
                    stack[-1][1] = max(stack[-1][1],intervals[i][1])
                else:
                    stack.append(intervals[i])
        return stack