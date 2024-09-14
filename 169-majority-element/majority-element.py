class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # use a hashmap to keep track of the frequency of elemtns 
        # then use hashmpa items to search for items which occur greater then n/2 
        # the moment you find them stop, searching since only 
        # one element can occure n/2 times. 
        import heapq
        from collections import Counter
        mapping = Counter(nums)
        pairs = [(-value,key) for (key, value) in mapping.items()]
        heapq.heapify(pairs)
        value, key = heapq.heappop(pairs)
        return key