class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        initial = list(range(1,k+1))
        def recurse(initial,current,n,k):
            if len(current) == k:
                ans.append(current)
                return 
            for i in range(1,n+1):
                if len(current) > 0:
                    if current[-1] < i:
                        recurse(initial,current+[i],n,k)
                else:
                    recurse(initial,current+[i],n,k)

            
        recurse(initial,[],n,k)
        return ans


            

