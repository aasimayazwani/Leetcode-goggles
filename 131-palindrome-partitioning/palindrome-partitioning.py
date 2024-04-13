class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack(s,cur):
            if len(s) == 0:
                ans.append(cur.split(","))
            else:
                backtrack(s[1:],cur +s[0])
                if len(cur) > 0:    
                    backtrack(s[1:],cur +","+s[0])
        backtrack(s,"")
        result = []
        for i in range(0,len(ans)):
            if self.gen(ans[i]):
                result.append(ans[i])
        return result 

    def valid(self,s):
        left = 0 
        right = len(s) - 1 
        while left <= right:
            if s[left] != s[right]:
                return False, s
            else:
                pass
            left +=1 
            right -=1
        return True, s

    def gen(self,arr):
        for i in range(0,len(arr)):
            if len(arr[i]) > 1:
                validity, string = self.valid(arr[i])
                if validity == False:
                    return False
                else:
                    pass
        return True

s = "aab"

