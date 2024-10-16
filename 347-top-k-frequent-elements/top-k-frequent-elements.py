class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter 
        import heapq
        mapping = Counter(nums)
        current = [(-value, key) for key, value in list(mapping.items())]
        heapq.heapify(current)
        answer = []
        while k > 0:
            value,key = heapq.heappop(current)
            k-=1
            answer.append(key)
        return answer