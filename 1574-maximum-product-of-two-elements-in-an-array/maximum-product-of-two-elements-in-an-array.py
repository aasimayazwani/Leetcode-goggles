class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums2 = [-item for item in nums]
        heapq.heapify(nums2)
        s1, s2 = heapq.heappop(nums2),heapq.heappop(nums2)
        return (-s1-1)*(-s2-1)