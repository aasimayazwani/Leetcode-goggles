class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        from collections import Counter
        mapping = Counter(nums)

        history = []
        while len(mapping.keys()) > 0:
            valid = list(mapping.keys())
            temp = (min(valid) + max(valid))/2
            history.append(temp)
            mapping[min(valid)] -=1 
            mapping[max(valid)] -=1 
            mapping = {key: value for key, value in mapping.items() if value > 0}

        answer = list(set(history))
        return len(answer)
