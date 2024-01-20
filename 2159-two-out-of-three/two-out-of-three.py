class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        nums3 = list(set(nums3))
        from collections import Counter
        total = nums1 + nums2 + nums3
        mapping = Counter(total)
        return [item[0] for item in mapping.items() if item[1] >= 2]