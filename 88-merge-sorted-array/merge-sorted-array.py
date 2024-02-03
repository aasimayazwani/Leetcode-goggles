class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        arr1 = nums1[0:m].copy()
        arr2 = nums2[0:n].copy()
        length = len(nums1)
        pointer1 = 0
        pointer2 = 0

        answer = []
        while pointer1 < len(arr1) and pointer2 < len(arr2):
            #print(arr1)
            if arr1[0] <= arr2[0]:
                answer.append(arr1[0])
                arr1 = arr1[1:]
                pass 
            else :
                answer.append(arr2[0])
                arr2 = arr2[1:]
                pass 
        
        nums1 += (answer + arr1 + arr2)
        del nums1[0:length]