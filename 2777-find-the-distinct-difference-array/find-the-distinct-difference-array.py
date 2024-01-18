class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
         # value - set()
        answer = []
        for i in range(0,len(nums)):
            total = len(list(set(nums[0:i+1]))) - len(list(set(nums[i+1:])))
            answer.append(total)
        return answer 