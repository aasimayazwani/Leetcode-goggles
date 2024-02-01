class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        arr1 = set()
        arr2 = set()
        result = []
        for i in range(0,len(A)):
            arr1.add(A[i])
            arr2.add(B[i])
            common = len(arr1.intersection(arr2))
            result.append(common)
        return result