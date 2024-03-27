class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(candidates,cur,target):
            cur = sorted(cur)
            if (target == 0) and (cur not in ans):
                ans.append(cur)
            if target > 0:
                for i in range(0,len(candidates)):
                    backtrack(candidates,cur+[candidates[i]],target - candidates[i])
        backtrack(candidates,[],target)
        #print(ans)
        return ans 