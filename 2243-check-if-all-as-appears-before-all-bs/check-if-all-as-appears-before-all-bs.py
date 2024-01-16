class Solution:
    def checkString(self, s: str) -> bool:
        mapping = {}
        for i in range(0,len(s)):
            if s[i] in mapping:
                mapping[s[i]].append(i)
            if s[i] not in mapping:
                mapping[s[i]] = [i]

        if "a" not in mapping:
            mapping["a"] = []
        if "b" not in mapping:
            mapping["b"] = []

        a_positions = mapping["a"]
        b_positions = mapping["b"]

        if len(a_positions) > 0 and len(b_positions) > 0:
            if max(a_positions) < min(b_positions):
                return True
            else:
                return False

        if len(a_positions) > 0 and len(b_positions) == 0:
            return True
        if len(a_positions) == 0 and len(b_positions) > 0:
            return True