class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        stack = []
        maximum = -1
        counting = 0 
        while nums:
            #print(stack)
            if len(stack) == 0:
                counting = 1 
                stack.append(nums[0])
                nums.pop(0)
            else:
                if nums[0] - stack[-1] == 1:
                    counting +=1 
                    stack.append(nums[0])
                    nums.pop(0)
                else:
                    maximum = max(maximum,counting)
                    stack = []
        maximum = max(maximum,counting)
        return maximum
                    