class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        # starting with index 0 as left 
        # index n -1 as right 
        # check if the nums[right] - nums[left] <
        result = []
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                for k in range(j,len(nums)):
                    if (nums[j]-nums[i] == diff) and (nums[k]-nums[j] == diff):
                        result.append((i,j,k))
        from collections import Counter
        t = Counter(result)
        return len(t.keys())