class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mapping = {}
        for i in range(0,len(nums1)):
            mapping[nums1[i][0]] = nums1[i][1]

        for i in range(0,len(nums2)):
            if nums2[i][0] in mapping:
                mapping[nums2[i][0]] = mapping[nums2[i][0]] + nums2[i][1]
            else:
                mapping[nums2[i][0]] = nums2[i][1]

        
        answers = list(mapping.items())
        return sorted(answers,key = lambda x:x[0])
        