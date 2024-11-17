# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.searching(root1) == self.searching(root2) 

    def searching(self,root):
        ans = []
        def dfs(root):
            if root == None:
                return []
            if root.left:
                dfs(root.left)
            if root.left == None and root.right == None:
                ans.append(root.val)
            if root.right:
                dfs(root.right)
        
        dfs(root)
        return ans