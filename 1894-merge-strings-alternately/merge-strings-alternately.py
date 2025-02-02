class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1, pointer2 = 0 ,0
        len1, len2 = len(word1), len(word2)
        answer = ""
        while pointer1 < len1 and pointer2 < len2:
            answer += word1[pointer1]
            pointer1 +=1

            answer += word2[pointer2]
            pointer2 +=1

        return answer + word1[pointer1:] + word2[pointer2:]
        

