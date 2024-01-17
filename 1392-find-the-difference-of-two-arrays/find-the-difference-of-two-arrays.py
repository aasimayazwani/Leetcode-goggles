class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        from collections import Counter
        nums1dict = Counter(nums1)
        nums2dict = Counter(nums2)

        ans1 = [item for item in list(nums1dict.keys()) if item not in [item for item in list(nums2dict.keys())] ] 
        ans2 = [item for item in list(nums2dict.keys()) if item not in [item for item in list(nums1dict.keys())] ] 
        return [ans1,ans2]