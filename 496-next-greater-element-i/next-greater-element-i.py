class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = [-1]*len(nums2)
        stack = []
        for i in range(0,len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                result[stack[-1]] = nums2[i]
                stack.pop(-1)
            stack.append(i)
        print(result)
        mapping = {}
        for i in range(0,len(nums2)):
            mapping[nums2[i]] = result[i]
        ans = []
        for j in range(0,len(nums1)):
            ans.append(mapping[nums1[j]])
        return ans