class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        import math
        import heapq
        gifts = [-item for item in gifts]
        nums = gifts.copy()
        heapq.heapify(nums)
        while k > 0:
            max_val = abs(heapq.heappop(nums))
            k-=1
            new_val = math.floor(math.sqrt(max_val))
            heapq.heappush(nums,-new_val)
        ans = []
        while nums:
            ans.append(abs(heapq.heappop(nums)))
        return sum(ans)