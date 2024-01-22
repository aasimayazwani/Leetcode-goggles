class Solution:
    def minSteps(self, s: str, t: str) -> int:
        from collections import Counter
        maps_s = Counter(s)
        maps_t = Counter(t)

        a = (maps_s-maps_t).values()
        b = (maps_t-maps_s).values()
        return sum([sum(a),sum(b)])