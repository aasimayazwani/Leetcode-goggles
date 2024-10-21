class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array first
        left, right = 0, len(nums) - 1
        counting = 0
        
        while left < right:
            total = nums[left] + nums[right]
            if total == k:
                # We found a pair, move both pointers inward
                counting += 1
                left += 1
                right -= 1
            elif total < k:
                # If the sum is less than k, move the left pointer to increase the sum
                left += 1
            else:
                # If the sum is greater than k, move the right pointer to decrease the sum
                right -= 1
        
        return counting
