class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(candidates,cur,target):
            if target == 0:
                cur = sorted(cur)
                if cur not in ans:
                    ans.append(cur)
            if target < 0:
                return 
            if target > 0:
                for i in range(0,len(candidates)):
                    backtrack(candidates,cur+[candidates[i]],target - candidates[i])
        
        backtrack(candidates,[],target)
        return ans 