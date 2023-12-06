class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        pairs = {}
        for size in range(minSize,maxSize+1):
            current = s[0:size-1]
            for i in range(size-1,len(s)):
                current = current + s[i]
                if self.count(current,maxLetters) == True:
                    if current in pairs:
                        pairs[current] +=1 
                    if current not in pairs:
                        pairs[current] = 1 
                    current = current[1:]
                else:
                    current = current[1:]
                    pass
        if pairs:   
            return max([item[1] for item in pairs.items()])
        if not pairs:
            return 0 


    def count(self, string, maxLetters):
        size = set()
        for i in range(len(string)):
            size.add(string[i])
            if len(size) > maxLetters:
                return False
        return True