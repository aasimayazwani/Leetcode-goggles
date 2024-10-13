# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get(root1) == self.get(root2)
        
    def get(self,root):
        points =[]
        def dfs(root):
            if root == None:
                return 
            dfs(root.left)
            if root.left == None and root.right == None:
                points.append(root.val)
            dfs(root.right)
        dfs(root)
        return points