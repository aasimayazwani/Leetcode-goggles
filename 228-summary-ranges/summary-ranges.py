class Solution:
    def summaryRanges(self, nums):
        if nums == []:
            return ""
        return self.get_pair(nums)
    
    def get_pair(self,nums):
        ans = []
        stack = []
        while len(nums) > 0:
            if len(stack) == 0:
                stack.append(nums.pop(0))
            else:
                if nums[0] - stack[-1] == 1:
                    stack.append(nums.pop(0))
                else:
                    if stack[0] != stack[-1]:
                        current = str(stack[0]) + "->" + str(stack[-1])
                        ans.append(current)
                        stack = []
                    else:
                        ans.append(str(stack.pop(0)))
        if len(stack)==1:
            ans.append(str(stack[0]))
        else:
            current = str(stack[0]) + "->" + str(stack[-1])
            ans.append(current)
        return ans