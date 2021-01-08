class Solution:
    def isAnagram(self,s, t):
        result_1 = self.dic(s)
        result_2 = self.dic(t)
        result_1.keys()==result_2.keys()
        if result_1.keys()!=result_2.keys():
            return False
        else:
            for item in list(set(s)):
                if result_1[item] != result_2[item]:
                    return False 
            return True    
    
    def dic(self,s):
        s = list(s)
        dictionary = {}
        for item in s:
            if item not in dictionary:
                dictionary[item]=0
            if item in dictionary:
                dictionary[item]+=1
        return dictionary