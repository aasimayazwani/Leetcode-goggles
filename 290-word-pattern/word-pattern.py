class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split the string s based on the empty spaces in s
        # use a hashmap to keep track of each pattern[index] -> s[index], if the key doesn't always exist it doesn't matter, 
        # but, if the key does exist already then the new value
        # must match the aready existing value pass, otherwise return false. 
        # if no failure is found return true. 
        mapping = {}
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
            
        status1 = self.check(pattern,s)
        status2 = self.check(s,pattern)
        answer= [status1,status2]
        if False in answer:
            return False 
        return True 
        

    def check(self,s,t):
        mapping = {}
        for i in range(0,len(s)):
            if s[i] in mapping:
                if mapping[s[i]] == t[i]:
                    pass 
                else:
                    return False
            if s[i] not in mapping:
                mapping[s[i]] = t[i]
        return True
