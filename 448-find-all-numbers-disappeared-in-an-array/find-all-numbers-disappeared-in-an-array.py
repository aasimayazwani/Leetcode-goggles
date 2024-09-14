class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        from collections import Counter
        mapping = Counter(nums)
        length = len(nums)
        answer = []
        for i in range(1,length+1):
            if i not in mapping:
                answer.append(i)
        return answer
