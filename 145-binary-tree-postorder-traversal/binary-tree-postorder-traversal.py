# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder = left, value, right
        # pre order = value, left, right
        # post order = left, right, Node
        ans = []
        def dfs(root):
            if root == None:
                return 
            else:
                dfs(root.left)
                dfs(root.right)
                ans.append(root.val)
        dfs(root)
        return ans 