class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        collect = []
        while len(nums) > 0:
            collect.append(heapq.heappop(nums))
        return collect 