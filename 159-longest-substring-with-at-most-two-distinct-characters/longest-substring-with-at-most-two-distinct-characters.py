class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) == 1:
            return 1 
        
        correct_strings = []
        for left in range(0,len(s)):
            new_string = s[left:]
            current = new_string[0]
            for i in range(1,len(new_string)):
                current = current + new_string[i]
                if self.check(current) == True:
                    correct_strings.append(current)
                else:
                    break
        return max([len(item) for item in correct_strings])


    def check(self,string):
        return len(set(string)) <= 2