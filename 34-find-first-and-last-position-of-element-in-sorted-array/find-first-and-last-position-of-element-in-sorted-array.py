class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        current = self.general(nums,target)
        if current != -1:
            r_edge = self.rsearch(nums,target,current,len(nums)-1)
            l_edge = self.lsearch(nums,target,0,current)
            return [l_edge,r_edge]
        return [-1,-1]
        
    def general(self,nums,target):
        left = 0 
        right = len(nums)- 1 
        while left <= right:
            mid = left + (right-left)//2 
            if target < nums[mid]:
                right = mid - 1 
            if target > nums[mid]:
                left = mid + 1 
            if target == nums[mid]:
                return mid
        return -1

    def rsearch(self,nums,target,left,right):
        while left <= right:
            mid = left + (right-left)//2
            if target >= nums[mid]:
                left = mid + 1
            if target < nums[mid]:
                right = mid - 1 
        return right

    def lsearch(self,nums,target,left,right):
        while left <= right:
            mid = left + (right-left)//2
            if target > nums[mid]:
                left = mid + 1
            if target <= nums[mid]:
                right = mid - 1 
        return left