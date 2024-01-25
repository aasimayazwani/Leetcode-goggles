class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        result = []
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if abs(nums[i]- nums[j]) <= min(nums[i],nums[j]):
                    result.append(nums[i]^nums[j])
        return max(result)

