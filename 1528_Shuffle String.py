class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        valu_dict = self.sorting(s,indices)
        new = sorted(list(valu_dict.keys()))
        string = ""
        for i in range(0,len(new)):
            string += valu_dict[new[i]]
        return string 
        
        
    def sorting(self,s,indices):
        temp = {}
        for i in range(0,len(indices)):
            temp[indices[i]] = s[i]
        return temp