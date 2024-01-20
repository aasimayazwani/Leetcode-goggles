class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(" ")
        
        broken = [item for item in brokenLetters]
        broken_dict = Counter(broken)
        keys = list(broken_dict.keys())

        counting = 0 
        for word in text:
            print(word)
            for i in range(0,len(keys)):
                if keys[i] in word :
                    #print(keys[i])
                    counting +=1 
                    break
        return len(text)-counting 
                