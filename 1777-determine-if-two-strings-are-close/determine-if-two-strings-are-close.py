class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        from collections import Counter
        mapping1 = Counter(word1)
        mapping2 = Counter(word2)
        difference = mapping1 - mapping2
        keys1 = set(mapping1.keys())
        keys2 = set(mapping2.keys())
        if len(keys1.difference(keys2)) > 0:
            return False
        else:
            if list(sorted(mapping1.values())) == list(sorted(mapping2.values())):
                return True 
            else:
                return False 