class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1, ptr2 = 0, 0 
        len1, len2 = len(nums1), len(nums2)
        while (ptr1 <  len1) and (ptr2 < len2):
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]
            elif nums1[ptr1] < nums2[ptr2]:
                ptr1 +=1 

            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 +=1 
        return -1 