class Solution:
    def insert(self, intervals, newInterval):
        intervals += [newInterval]
        intervals = sorted(intervals,key=lambda x:x[0])
        print(intervals)
        stack= []
        while intervals:
            if len(stack) == 0:
                stack.append(intervals[0])
                intervals.pop(0)
            else:
                if stack[-1][1] >= intervals[0][0]:
                    previous = stack.pop(-1)
                    new = [previous[0],max(previous[1],intervals[0][1])]
                    intervals.pop(0)
                    stack.append(new)
                else:
                    stack.append(intervals[0])
                    intervals.pop(0)
        return stack