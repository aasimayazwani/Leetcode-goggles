# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(root):
            if root == None:
                return 
            else:
                dfs(root.left)
                result.append(root.val)
                dfs(root.right)
            return result
        return dfs(root)