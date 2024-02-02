class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals,key=lambda x:x[0])
        stack = []
        for i in range(0,len(intervals)):
            #print(stack)
            if len(stack) == 0:
                stack.append(intervals[i])
            else:
                if stack[-1][1] > intervals[i][0]:
                    return False 
                else:
                    stack.append(intervals[i]) 
        return True