class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [item for item in s.split(" ") if len(item) > 0][-1]

        return len(words)