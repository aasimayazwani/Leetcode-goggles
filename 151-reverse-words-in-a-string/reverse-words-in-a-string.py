class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([item for item in s.split(" ") if item != ""][::-1])
        