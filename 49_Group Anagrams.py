class Solution:
    def groupAnagrams(self,strs):
        array_dict = []
        for i in range(0,len(strs)):
            array_dict.append(self.dictionary(strs[i]))
        
        merged = []
        current = []
        for i in range(0,len(array_dict)):
            #current.append(strs[i])
            for j in range(0,len(array_dict)):
                    if array_dict[i] == array_dict[j]:
                        current.append(strs[j])
            sor_cur = sorted(current)
            if sor_cur not in merged:
                merged.append(sor_cur)
            current = []
        return merged 
    
    
    def dictionary(self,strs):    
        strs = [item for item in strs]
        A = dict()
        for i in range(0,len(strs)):
            if strs[i] not in A:
                A[strs[i]]= 1 
            else:
                A[strs[i]]+= 1 
        return A 
