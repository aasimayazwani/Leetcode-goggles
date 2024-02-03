class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        var = [[int(item) for item in str(items)] for items in nums]
        answer = []
        for i in range(0,len(var)):
            answer.extend(var[i])
        return answer 