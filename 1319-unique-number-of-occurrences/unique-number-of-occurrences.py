class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        mapping = Counter(arr)
        return len(mapping.keys())  == len(set([item[1] for item in list(mapping.items())]))