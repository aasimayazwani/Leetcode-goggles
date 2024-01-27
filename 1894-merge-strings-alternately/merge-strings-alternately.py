class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # EDGE CASES
        # if len(word1) > 0 and len(word2) > 0 
        # if len(word1) ==0 and len(word2) > 0 
        # if len(word2) == 0  and len(word1) > 0 
        
        # we will create a pointer for each of the words, word1[[pointer]] + word2[pointer]
        # move them after each addition
        # stop the process if either of the strings are of zero length 

        pointer1 = 0 
        pointer2 = 0 
        result = ""
        while (pointer1 < len(word1)) and (pointer2  <len(word2)):
            result += word1[pointer1] + word2[pointer2]
            pointer1 +=1 
            pointer2 +=1 
        result += word1[pointer1:] + word2[pointer2:]
        return result 