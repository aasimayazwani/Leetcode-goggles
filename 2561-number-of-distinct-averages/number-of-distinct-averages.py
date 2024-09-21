class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums = sorted(nums)
        left = 0
        right = len(nums)-1
        answer = set()
        while left < right:
            answer.add((nums[left]+nums[right])/2)
            left +=1 
            right -=1 
        return len(answer)