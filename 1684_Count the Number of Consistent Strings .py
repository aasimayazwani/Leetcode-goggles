class Solution:
    def countConsistentStrings(self, allowed, words):
        allowed_dict = set(allowed)
        temp = 0
        for i in range(0,len(words)):
            if len(set(words[i])-allowed_dict) == 0 :
                temp +=1 
            else:
                pass 
        return temp