class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-item for item in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            st1, st2 = heapq.heappop(stones), heapq.heappop(stones)
            st1, st2 = -st1, -st2
            if st1 == st2:
                pass # both the stones get destroyed
            else:
                new_weight = abs(st2-st1)
                heapq.heappush(stones,-new_weight)
        if len(stones) == 1:
            s = heapq.heappop(stones)
            return -s 
        return 0 
            
