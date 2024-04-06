class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(candidates,current,target):
            if target == 0:
                current = sorted(current)
                if current not in result:
                    result.append(current)
            if target < 0:
                return 
            if target > 0:
                for i in range(0,len(candidates)):
                    backtrack(candidates,current+[candidates[i]],target -candidates[i])
        backtrack(candidates,[],target)
        return (result)