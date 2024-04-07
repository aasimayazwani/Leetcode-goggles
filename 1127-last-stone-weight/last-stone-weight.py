class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-item for item in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = -(heapq.heappop(stones))
            y = -(heapq.heappop(stones))
            if x < y:
                heapq.heappush(stones,-(y-x))
            if y < x:
                heapq.heappush(stones,-(x-y))

        if len(stones) == 1:
            return -(stones[0])
        return 0