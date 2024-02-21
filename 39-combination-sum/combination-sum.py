class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def iterate(arr,target,candidates):
            if target == 0:
                arr =sorted(arr)
                if arr not in answer:
                    answer.append(arr)
            if target < 0:
                pass

            if target > 0:
                for i in range(0,len(candidates)):
                    current = candidates[i]
                    iterate(arr + [current],target - current,candidates)

        answer = []
        iterate([],target,candidates)
        return answer