class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter 
        mapping = {}
        for i in range(0,len(nums2)):
            mapping[nums2[i]] = i
        answer = []
        for i in range(0,len(nums1)):
            answer.append(mapping[nums1[i]])
        return answer