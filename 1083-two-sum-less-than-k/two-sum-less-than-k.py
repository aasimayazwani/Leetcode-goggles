class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        values = [-1]
        left, right = 0, len(nums)-1
        while left < right:
            cur_sum = nums[left] + nums[right]
            if cur_sum >= k:
                right -=1 
            if cur_sum < k:
                values.append(cur_sum)
                left +=1
        return max(values)