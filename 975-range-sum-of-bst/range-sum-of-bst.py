# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = []
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            if root.val >= low and root.val <= high:
                total.append(root.val)
            dfs(root.right)
        dfs(root)
        return sum(total)