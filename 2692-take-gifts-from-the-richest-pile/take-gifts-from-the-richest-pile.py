class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-item for item in gifts]
        heapq.heapify(gifts)
        while k > 0:
            current = heapq.heappop(gifts)
            k -=1
            heappush(gifts,-math.floor(math.sqrt(-(current))))
        total = []
        while len(gifts) > 0:
            total.append(heapq.heappop(gifts))
        return -sum(total)