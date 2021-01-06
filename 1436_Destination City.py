class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for i in range(0,len(paths)):
            key = paths[i][0]
            value = paths[i][1]
            if i == 0 :
                r = dict()
                r = self.dictionary(key,value,r)
            else:
                r = self.dictionary(key,value,r)
            
        for path in paths:
            if path[1] not in r:
                return path[1]
            
    def dictionary(self,element,value,dicti):
        if dicti == None:
            dicti = dict()
        else:
            dicti = dicti
            if element not in dicti:
                dicti[element] = value 
        return dicti