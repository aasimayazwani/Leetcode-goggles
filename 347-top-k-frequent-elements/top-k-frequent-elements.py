class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        mapping = Counter(nums)
        maps = [(-item,key) for key,item in mapping.items()]
        heapq.heapify(maps)
        ans = []
        while k > 0:
            current = heapq.heappop(maps)
            ans.append(current[1])
            k-=1
        return ans 