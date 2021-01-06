class Solution:
    def romanToInt(self, s):
        s = [item for item in s]
        temp = self.mapping()
        value = 0 
        while s:
            if len(s) > 1:
                if temp[s[1]] > temp[s[0]] :
                    value += temp[s[1]] - temp[s[0]]
                    del s[0:2]
                else:
                    value += temp[s[0]]
                    del s[0]
            else :
                value += temp[s[0]]
                return value
        return value 

    def mapping(self):
        symbol = ["I","V","X","L","C","D","M"]
        value =  [1,5,10,50,100,500,1000]
        temp = {}
        for i in range(0,len(symbol)):
            temp[symbol[i]] = value[i]
        return temp