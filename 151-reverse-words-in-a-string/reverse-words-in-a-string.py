class Solution:
    def reverseWords(self, s: str) -> str:
        s= [item for item in s.split(" ") if item != ""]
        s = " ".join(s[::-1])
        return s