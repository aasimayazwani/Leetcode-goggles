# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(root):
            if root == None:
                return 0
            else:
                left_sum = dfs(root.left)
                right_sum = dfs(root.right)

                values.append(abs(left_sum - right_sum))

                return root.val + left_sum + right_sum 

        dfs(root)
        return sum(values)