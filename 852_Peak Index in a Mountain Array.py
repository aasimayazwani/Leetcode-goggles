class Solution:
    def peakIndexInMountainArray(self, A: List[int]):
        greater = A[0]
        for i in range(0,len(A)):
            if A[i]> greater:
                greater = A[i]
        for i in range(0,len(A)):
            if A[i] == greater:
                return i 