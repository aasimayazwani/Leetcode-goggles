class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        mapping = Counter(s)
        values = [(-freq,char) for char, freq in mapping.items()]
        result = []
        heapq.heapify(values)
        while len(values) > 0:
            freq, character = heapq.heappop(values)
            result += character*abs(freq)
        return result