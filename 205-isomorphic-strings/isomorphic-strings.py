class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # logic
        # This is a recurring theme in many questions. 
        # the question provides two strings where the position of the individial mapping 
        # is important is important and neither the succesor and previous elements. 
        # Remember that not only should the mapping of s -> t must be unique, but also t-> s
        status1 = self.check(t,s)
        status2 = self.check(s,t)
        answer = [status1,status2]
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