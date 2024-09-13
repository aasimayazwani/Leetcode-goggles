class Solution:
    def wordPattern(self, pattern, s):
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        mapping ={}
        first_check = True
        for i in range(0,len(pattern)):
            current = pattern[i]
            if current not in mapping:
                mapping[current] = s[i]
            else:
                if mapping[current] != s[i]:
                    first_check = False
                    break
        
        second = {}
        second_check = True
        for i in range(0,len(s)):
            if s[i] not in second:
                second[s[i]] = pattern[i]
            else:
                if second[s[i]] != pattern[i]:
                    second_check = False
        if False in [second_check,first_check]:
            return False
        return True