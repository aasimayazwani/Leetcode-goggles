class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #import heapq 
        from collections import Counter
        mapping = Counter(words)
        min_heap = [(-freq, value) for value, freq in mapping.items()]
        heapq.heapify(min_heap)
        result = []
        for i in range(0,k):
            freq, words = heapq.heappop(min_heap)
            result.append(words)
        return result