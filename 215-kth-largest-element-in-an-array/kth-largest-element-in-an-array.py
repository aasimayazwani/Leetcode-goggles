class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify
        nums = [-item for item in nums]
        heapify(nums)
        while k > 0:
            temp = heapq.heappop(nums)
            k = k -1 
        return -temp