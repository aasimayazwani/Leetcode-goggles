class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squared = [m*n for m,n in zip(A,A)]
        squared.sort()
        return squared