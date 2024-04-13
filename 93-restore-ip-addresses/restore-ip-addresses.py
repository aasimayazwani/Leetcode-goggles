class Solution:
    def restoreIpAddresses(self, s):
        def iterate(s,current,counting):
            if len(s) == 0:
                if counting == 3:
                    ans.append(current)
            else:
                iterate(s[1:],current+s[0]+".",counting +1)
                #iterate(s[2:],current+s[0:2] + ".",counting +1)
                #iterate(s[2:],current+s[0:2],counting)
                iterate(s[1:],current+s[0],counting)

        ans =[]
        #s = "101023"
        iterate(s,"",0)

        result = set()
        for i in range(0,len(ans)):
            status, original = self.check(ans[i])
            if status == True:
                result.add(original)
        
        result = list(result)
        total = []
        for i in range(0,len(result)):
            status, current = self.leading_zero(result[i])
            if status == True:
                total.append(current)
        return total

    def check(self,current):
        try:
            string = [int(item) for item in current.split(".")]
            if (min(string) >= 0) and (max(string) <= 255):
                return True, current
            return False, current
        except:
            return False, current

    def leading_zero(self,current):
        string = [item for item in current.split(".")]
        for i in range(0,len(string)):
            if (len(string[i]) >= 2) and (string[i][0] == "0") :
                return False,current
        return True, current