class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        from collections import Counter
        import math
        mapping = Counter(s)
        return math.floor((mapping[letter]*100)/len(s))