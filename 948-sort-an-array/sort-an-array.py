class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ans = []
        import heapq 
        heapq.heapify(nums)
        while nums:
            current = heapq.heappop(nums)
            ans.append(current)
        return ans