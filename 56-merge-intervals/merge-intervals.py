class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x:x[0])
        stack  = []
        while len(intervals) > 0:
            if len(stack) == 0:
                stack.append(intervals[0])
                intervals.pop(0)
            else:
                if intervals[0][0] <= stack[-1][1]:
                    new = [stack[-1][0],max(intervals[0][1],stack[-1][1])]
                    stack.pop(-1)
                    stack.append(new)
                    intervals.pop(0)
                else:
                    stack.append(intervals[0])
                    intervals.pop(0)
        print(stack)
        return stack
                    