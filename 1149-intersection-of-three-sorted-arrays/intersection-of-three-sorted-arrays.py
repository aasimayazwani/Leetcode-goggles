class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        from collections import Counter
        arr1_dict = Counter(arr1)
        arr2_dict = Counter(arr2)
        arr3_dict = Counter(arr3)

        common = [item for item in list(arr1_dict.keys()) if item in list(arr2_dict.keys())] 
        return [item for item in list(arr3_dict.keys()) if item in common]