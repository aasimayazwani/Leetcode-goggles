class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return "".join([item[0] for item in words]) == s