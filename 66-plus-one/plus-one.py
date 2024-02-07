class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits= "".join([str(item) for item in digits])
        digits = str(int(digits) + 1 )
        return [int(item) for item in digits]