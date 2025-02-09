class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        length  = 2*n
        left = ["(","[","{"]
        right = [")","]","}"]
        mapping = {}
        for i in range(0,len(right)):
            mapping[left[i]] = right[i]

        def check(s):
            stack = []
            s = [item for item in s ]
            while len(s):
                if len(stack) == 0:
                    if s[0] in left:
                        stack.append(s.pop(0))
                    else:
                        return False 
                else:
                    if s[0] in left:
                        stack.append(s.pop(0))
                    elif s[0] in right:
                        if mapping[stack[-1]] == s[0]:
                            s.pop(0)
                            stack.pop(-1)
                        else:
                            return False
            if len(stack) == 0:
                return True
            return False 

        def create(string,length,left,right):
            if length == 0:
                if left == right:
                    ans.append(string)
                return 
            else:
                #create( "("+string,length-1, left +1, right)
                #create( ")"+string,length-1, left, right+1)
                create( string+")",length-1, left, right+1)
                create( string+"(",length-1, left+1, right)
        
        ans = []
        result = []
        create("",length,0,0)
        #print(ans)

        for i in range(0,len(ans)):
            if check(ans[i]):
                result.append(ans[i])
        return list(set(result) )
        
        