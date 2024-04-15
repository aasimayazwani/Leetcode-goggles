class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = self.general(nums,target)
        if pos == -1:
            return [-1,-1]
        else:
            l = self.lsearch(nums,0,pos,target)
            r = self.rsearch(nums,pos,len(nums)-1,target)
            return [l,r]
        
    def general(self,nums,target):
        left, right = 0 ,len(nums)-1
        while left <= right:
            mid = left + (right - left)//2
            if target < nums[mid]:
                right = mid - 1 
            elif target > nums[mid]:
                left = mid + 1 
            else:
                return mid
        return -1

    def lsearch(self,nums,left,right,target):
        while left <= right:
            print(nums[left:right+1])
            mid = left + (right - left)//2 
            if target > nums[mid]:
                left = mid + 1 
            if target <= nums[mid]:
                right = mid - 1
        return left 

    def rsearch(self,nums,left,right,target):
        while left <= right :
            print(nums[left:right+1])
            mid = left + (right-left)//2 
            if target >= nums[mid]:
                left = mid + 1 
            if target < nums[mid]:
                right = mid - 1 
        return right