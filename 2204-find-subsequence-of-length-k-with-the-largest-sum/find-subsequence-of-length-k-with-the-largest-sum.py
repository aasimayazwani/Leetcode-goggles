class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        for i in range(0,len(nums)):
            heapq.heappush(min_heap,(nums[i],i))
        result = heapq.nlargest(k,min_heap)
        result = sorted(result,key= lambda x:x[1],reverse = False)
        return [item[0] for item in result]