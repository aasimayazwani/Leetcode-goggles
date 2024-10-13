# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        mapping = {}
        if root == None:
            return False 
        
        def dfs(root,current):
            if root == None:
                return 
            else:
                dfs(root.left,current+root.val)
                if root.left == None and root.right == None:
                    mapping[current+root.val] = 1
                dfs(root.right,current+root.val)
        dfs(root,0)
        if targetSum in mapping:
            return True 
        return False 