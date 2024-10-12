class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1, word2 = [item for item in word1], [item for item in word2]
        answer = ""
        while len(word1) > 0 and len(word2) > 0:
            answer += word1.pop(0)
            answer += word2.pop(0)
        return "".join(answer) + "".join(word1) + "".join(word2)