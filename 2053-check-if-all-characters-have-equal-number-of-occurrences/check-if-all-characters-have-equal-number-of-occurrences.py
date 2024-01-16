class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import Counter 
        dictionary = Counter(s)
        return len(set([item[1] for item in list(dictionary.items())])) == 1