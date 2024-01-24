class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        candies = [item+extraCandies for item in candies]
        return [True if item >= maximum else False for item in candies]