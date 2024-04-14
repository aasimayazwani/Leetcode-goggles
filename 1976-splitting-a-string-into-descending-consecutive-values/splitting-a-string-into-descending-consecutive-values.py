class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(s,current,index):
            if index == len(s):
                t = [int(item) for item in current.split(",")]
                if len(t) > 1:
                    ans.append(t)
            else:
                backtrack(s,current + s[index],index +1)
                if len(current) > 0:
                    items = current.split(",")
                    if len(items) >= 2:
                        items = items[-2:]
                        if int(items[0]) - int(items[1]) == 1:
                            backtrack(s,current + "," +s[index],index+1)
                    else:
                        backtrack(s,current + "," +s[index],index+1)
        
        ans = []
        backtrack(s,"",0)
        #print(ans)
        for i in range(0,len(ans)):
            current = ans[i]
            if self.get(current) == True:
                #print(current)
                return True
        return False

    def get(self,current):
        for j in range(0,len(current)-1):
            if current[j] - current[j+1] == 1:
                pass 
            else :
                return False
        return True