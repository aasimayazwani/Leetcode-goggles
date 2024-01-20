class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        min1,min2 = nums1[0], nums2[0]

        try:
            candidate = min([item for item in nums1 if item in nums2])
        except:
            candidate = 100000

        answer = ""
        if min2 < min1:
            answer += str(min2) + str(min1)
            return min(int(answer),candidate)
        else:
            answer += str(min1) + str(min2)
            return min(int(answer),candidate)
            
