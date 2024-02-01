class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals = intervals + [newInterval]
        intervals = sorted(intervals,key=lambda x:x[0])
        stack = []
        for i in range(0,len(intervals)):
            if len(stack) == 0:
                stack.append(intervals[i])
            else:
                if intervals[i][0] <=  stack[-1][1]:
                    stack[-1][1] = max(intervals[i][1],stack[-1][1])
                else:
                    stack.append(intervals[i])
        return stack