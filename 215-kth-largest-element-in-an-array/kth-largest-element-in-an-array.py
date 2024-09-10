class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-item for item in nums]
        import heapq 
        heapq.heapify(nums)
        while k > 1:
            heapq.heappop(nums)
            k-=1
        ans = heapq.heappop(nums)
        return -ans 