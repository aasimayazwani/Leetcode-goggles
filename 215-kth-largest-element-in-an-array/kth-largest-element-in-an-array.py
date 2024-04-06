class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        current = nums[0:k]
        heapq.heapify(current)
        rest = nums[k:]
        for num in rest:
            heapq.heappush(current,num)
            heapq.heappop(current)
        return current[0]