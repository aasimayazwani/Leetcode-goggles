import heapq
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        length = len(nums)
        score = 0
        marked = set()  # Use a set for O(1) lookups
        heap = [(nums[i], i) for i in range(length)]  # Min-heap initialization
        heapq.heapify(heap)  # O(n) heap construction
        
        while heap:
            val, pos = heapq.heappop(heap)
            if pos in marked:
                continue  # Skip if already removed
            
            score += val
            marked.add(pos)

            # Mark neighbors for removal
            for neighbor in [pos - 1, pos + 1]:
                if 0 <= neighbor < length and neighbor not in marked:
                    marked.add(neighbor)
        
        return score
