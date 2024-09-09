class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtracking(current, original,total):
            if len(current) == total:
                ans.append(current)
                return 
            if len(current) < total:
                for i in range(0,len(original)):
                    if len(current) == 0:
                        backtracking(current +[original[i]],original,total)
                    if len(current) > 0:
                        if original[i] not in current:
                            backtracking(current +[original[i]],original,total)

        ans = []

        total = len(nums)
        backtracking([],nums,total)
        return ans