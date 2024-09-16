class Solution:
    def specialArray(self, nums: List[int]) -> int:
        k = len(nums)
        """
        It should be clear that the upper limit of the k value is going to be since that is the 
        size of the array. so best case every element in the array is above that size constraint. 
        if that is not the case keep on reducing the size of k. 
        """
        while k > 0:
            #print(k)
            if len([item for item in nums if item >= k]) == k:
                return k 
            else:
                k -=1 
        return -1 