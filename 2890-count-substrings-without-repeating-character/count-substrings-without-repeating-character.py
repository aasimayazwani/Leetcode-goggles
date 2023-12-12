class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        mapping = self.generate(s)

        count = 0
        for left in range(0,len(s)):
            cur = set()
            for i in range(left,len(s)):
                if mapping[i] not in cur:
                    cur.add(mapping[i])
                    count +=1 
                else:
                    break
        return count
    
    def check_unique(self,string):
        current = set()
        for i in range(0,len(string)):
            if string[i] in current:
                return False
            if string[i] not in current:
                current.add(string[i]) 
        return True

    def generate(self,string):
        mapping = {}
        for i in range(0,len(string)):
            mapping[i] = string[i]
        return mapping
