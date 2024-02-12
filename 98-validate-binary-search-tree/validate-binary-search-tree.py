# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root):
        values = []
        
        def dfs(root):
            if root == None:
                return []
            else:
                dfs(root.left)
                values.append(root.val)
                dfs(root.right)

            return values
                
        dfs(root)
        if len(set(values)) < len(values):
            return False
        elif sorted(values) == list(values):
            return True
        return False 