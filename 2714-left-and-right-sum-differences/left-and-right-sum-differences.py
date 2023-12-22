class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = []
        rightSum = []
        answer = []
        nums_reversed = list(reversed(nums))
        if len(nums) == 0:
            return [0]
        else:
            for i in range(len(nums)):
                leftSum.append(sum(nums[0:i]))
            for i in range(len(nums_reversed)):
                rightSum.append(sum(nums_reversed[0:i]))
            leftSum_reversed = list(reversed(leftSum))
            for i, j in zip(leftSum_reversed, rightSum):
                answer.append(abs(i-j))

                    
        return list(reversed(answer))


        