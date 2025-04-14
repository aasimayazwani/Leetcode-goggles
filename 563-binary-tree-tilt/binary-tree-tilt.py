# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(root):
            if root == None:
                return 0
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            self.total += abs(left_sum - right_sum)
            return left_sum + right_sum + root.val 
        
        dfs(root)
        return self.total

