class Solution:
    def reverseWords(self, s: str) -> str:
        some = []
        for i in range(0,len(s.split(" "))):
            some.append((s.split(" ")[i][::-1]))
        return " ".join(some)