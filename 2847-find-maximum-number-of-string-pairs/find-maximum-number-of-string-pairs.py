class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        arr = set()
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if words[i] == words[j][::-1]:
                    if (words[i] not in arr) and (words[j] not in arr):
                        arr.add(words[i])
                    else:
                        pass 
        return len(arr)