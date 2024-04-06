class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap = []
        for i in range(0,len(nums)):
            heappush(min_heap,int(nums[i]))
        return str(heapq.nlargest(k,min_heap)[-1])
