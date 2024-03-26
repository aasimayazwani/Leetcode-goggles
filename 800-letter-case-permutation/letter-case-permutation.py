class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(s,current,index):
            print(current)
            if len(current) == len(s):
                ans.append(current)
            else:
                if s[index].isalpha() == True:
                    backtrack(s,current+s[index].upper(),index+1)
                    backtrack(s,current+s[index].lower(),index+1)
                else:
                    backtrack(s,current+s[index],index+1)
        backtrack(s,"",0)
        #print(ans)
        return ans 
    