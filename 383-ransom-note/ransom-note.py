class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # logic
        # The questions is only asking if the string entries present 
        # in the ranson note are less then or equal to the magazine. 
        # THe order is not relevant
        # so I will use a dictionary for both the magazine and ransomnote. 

        from collections import Counter
        ransom_dict = Counter(ransomNote)
        magazine_dict = Counter(magazine)

        words = set(ransomNote)
        for word in words:
            if ransom_dict[word] > magazine_dict[word]:
                return False
            else:
                pass 
        return True 