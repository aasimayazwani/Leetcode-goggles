class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        while k  > 0 :
            nums.insert(0,nums[-1])
            del nums[-1]
            k = k -1 