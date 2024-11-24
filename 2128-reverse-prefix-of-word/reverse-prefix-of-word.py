class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = [item for item in word]
        stack = []
        for i in range(0,len(word)):
            if word[i] == ch:
                stack.append(ch)
                return "".join(stack[::-1]) + "".join(word[i+1:])
            elif word[i] != ch:
                stack.append(word[i])
        return "".join(word)
            
