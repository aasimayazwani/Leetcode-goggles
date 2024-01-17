class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        from collections import Counter
        mapping = Counter(arr)
        unique = set([item[0] for item in mapping.items() if item[1] == 1])

        for i in range(0,len(arr)):
            if arr[i] in unique:
                if k == 1:
                    return arr[i]
                else:
                    k = k - 1
        return ""
    