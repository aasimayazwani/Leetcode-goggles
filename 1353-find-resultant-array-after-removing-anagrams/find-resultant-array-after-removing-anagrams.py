class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        from collections import Counter
        stack = []
        for i in range(0,len(words)):
            if (len(stack) > 0) and (Counter(words[i]) ==Counter(stack[-1])):
                pass 
            else:
                stack.append(words[i])
        return stack 