# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(left,right,nums):
            if left > right:
                return 
            mid = left + (right-left)//2 
            root = TreeNode(nums[mid])
            root.left = dfs(left,mid-1,nums)
            root.right = dfs(mid+1,right,nums)
            return root
        
        return dfs(0,len(nums)-1,nums)