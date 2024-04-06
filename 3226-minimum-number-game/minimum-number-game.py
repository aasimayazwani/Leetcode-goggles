class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        result = []
        while len(nums) > 0:
            alice = heapq.heappop(nums)
            bob = heapq.heappop(nums)
            result += [bob,alice]
        return result 