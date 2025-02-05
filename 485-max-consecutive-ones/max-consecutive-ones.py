class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        values = 0
        stack = [] 
        while len(nums) > 0:            
            if nums[0] == 1:
                stack.append(nums.pop(0))
            else:
                values = max(values,len(stack))
                print("stack is ",stack)
                nums.pop(0)
                stack = []
        return max(values,len(stack))
                