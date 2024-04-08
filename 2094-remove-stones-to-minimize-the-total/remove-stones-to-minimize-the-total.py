class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-item for item in piles]
        
        heapq.heapify(piles)
        while k > 0:
            x = heapq.heappop(piles)
            heapq.heappush(piles,math.floor(x/2))
            k-=1 
        total = 0
        while piles:
            total += abs(heapq.heappop(piles))
        return total 