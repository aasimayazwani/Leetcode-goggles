class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        temp = []
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] == nums[j] and i<j :
                    temp.append(i)
        return len(temp)