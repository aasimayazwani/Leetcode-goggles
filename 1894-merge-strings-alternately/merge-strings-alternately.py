class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # EDGE CASES
        # if len(word1) > 0 and len(word2) > 0 
        # if len(word1) ==0 and len(word2) > 0 
        # if len(word2) == 0  and len(word1) > 0 
        
        # we will create a pointer for each of the words, word1[[pointer]] + word2[pointer]
        # move them after each addition
        # stop the process if either of the strings are of zero length 

        answer = ""
        while True:
            if len(word1) > 0:
                answer += word1[0]
                word1 = word1[1:]
            if len(word2) > 0:
                answer += word2[0]
                word2 = word2[1:]
            else:
                break
        return answer + word1 + word2