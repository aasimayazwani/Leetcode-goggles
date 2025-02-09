class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1,n+1))
        def search(cur,k):
            if len(cur) == k:
                ans.append(cur)
                return 
            else:
                for i in range(1,n+1):
                    if len(cur) ==0:
                        search(cur+[i],k)
                    else:
                        if cur[-1] < i:
                            search(cur+[i],k)
        ans = []
        search([],k)
        return ans 
            
