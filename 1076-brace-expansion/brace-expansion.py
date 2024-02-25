class Solution:
    def expand(self, s: str) -> List[str]:
        def recurse(string,s):
            if len(s) == 0:
                ans.append(string)
            else:
                if s[0] != "{":
                    recurse(string + s[0],s[1:])

                if s[0] == "{":
                    for i in range(1,len(s)):
                        if s[i] == "}":
                            break
                    for j in range(1,i):
                        if s[j] != ",":
                            recurse(string+s[j],s[i+1:])
        ans = []
        recurse("",s)
        return sorted(ans)
            
                        
