class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""

        edge1 = len(word1) - 1
        pointer1 = 0 

        edge2 = len(word2) - 1
        pointer2 = 0

        while (pointer1 <= edge1) and (pointer2 <= edge2) :
            if len(word1) > 0:
                answer += word1[pointer1]
                pointer1 +=1
            if len(word2) > 0:
                answer += word2[pointer2]
                pointer2 +=1

        return answer + word1[pointer1:] + word2[pointer2:]
        