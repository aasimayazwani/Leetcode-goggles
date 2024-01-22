class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        part1 = sum(nums)
        part2 = sum([sum([int(value) for value in str(item)]) if len(str(item)) > 0 else item for item in nums])
        return part1 - part2