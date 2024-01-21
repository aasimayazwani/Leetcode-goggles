class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        from collections import Counter
        import math

        mapping = Counter(s)
        target_dict = Counter(target)
        keys = list(target_dict.keys())
        answer = []

        for i in range(0,len(keys)): 
            answer.append(math.floor(mapping[keys[i]]/target_dict[keys[i]]))

        return min(answer)