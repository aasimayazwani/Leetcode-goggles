class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length = len(s)
        max_length =  0
        score = {"a":1,"e":2,"i":1,"o":2,"u":1}
        current = s[0:k-1]
        counting = self.get_count(current)
        for i in range(k-1,length):   
            current = current + s[i]
            #print(current)
            if current[-1] in score:
                counting +=1
            else:
                pass 
            max_length = max(counting,max_length)
            if current[0] in score:
                counting -=1
            else:
                pass
            current = current[1:]
                

        return max_length


    def get_count(self,s):
        score = {"a":1,"e":2,"i":1,"o":2,"u":1}
        total = 0
        
        for i in range(0,len(s)):
            
            if s[i] in score:
                total += 1
            if s[i] not in score:
                total += 0 
        return total 