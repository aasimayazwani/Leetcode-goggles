class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1 = [item for item in word1]
        word2 = [item for item in word2]
        result = ""
        index = 0
        while index < len(word1) and index < len(word2) :
            result += word1[index] + word2[index]
            index +=1 
        return result + "".join(word1[index:]) + "".join(word2[index:])