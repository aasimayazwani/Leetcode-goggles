class Solution:
    def letterCombinations(self, digits):
        dig = [int(item) for item in digits]
        let = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        if len(digits) ==0:
            return  ""
        if len(digits) ==1:
            return [item for item in let[digits]]
        else:
            temp = []
            for i in range(0,len(dig)):
                temp.append(let[str(dig[i])])
            ser = [item for item in temp[0]]
            res = []
            for i in range(0,len(temp[1])):
                res.extend([item + temp[1][i] for item in ser])
            if len(dig) ==2:
                return res 
            else:
                left = digits[2:]
                current = []
                for i in range(0,len(left)):
                    t = let[left[i]]
                    for j in range(0,len(t)):
                        current.extend([item + t[j] for item in res])
                    res = current 
                    current = []
                return res