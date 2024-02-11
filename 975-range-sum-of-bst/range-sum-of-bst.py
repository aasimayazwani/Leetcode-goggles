# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = []
        def dfs(root):
            if root == None:
                return 
            else:
                dfs(root.left)
                if low <= root.val <= high:
                    result.append(root.val)
                dfs(root.right)

            return result
        total = dfs(root)
        return sum(total)