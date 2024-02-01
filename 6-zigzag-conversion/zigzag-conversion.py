class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        stack = []
        i = 0
        while len(s) > 0:
            if i%2 == 0:
                stack.append(s[0:numRows])
                s = s[numRows:]
            else:
                stack.append(s[0:numRows-2])
                s = s[numRows-2:]
            i +=1
            
        second = []
        for i in range(0,len(stack)):
            if i %2 != 0:
                second.extend(self.get_words(stack[i],numRows))
            else:
                second.append(stack[i])
                
                
        for i in range(0,len(second)):
            if len(second[i]) < numRows:
                second[i] = second[i] + "*"*(numRows - len(second[i]))
                
        answer = []
        for i in range(0,numRows):
            answer.append("".join([item[i] for item in second if item[i] != "*"]))
            
        return "".join(answer)

    def get_words(self,words,numRows):
        collection = []
        for i in range(0,len(words)):
            new_word = "*"*(i+1) + words[i] + "*"*(numRows-i-2)
            collection.append(new_word[::-1])
        return collection