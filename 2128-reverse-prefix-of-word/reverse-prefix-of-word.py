class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = [item for item in word]
        for i in range(0,len(word)):
            if word[i] == ch:
                return self.reversing(word,0,i)
        return "".join(word)
    
    def reversing(self,word,left,right):
        while left < right:
            word[left], word[right] = word[right], word[left]
            left +=1 
            right -=1 
        return "".join(word)