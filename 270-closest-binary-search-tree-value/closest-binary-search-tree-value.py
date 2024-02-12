# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        values = []
        def dfs(root):
            if root == None:
                return 
            else:
                dfs(root.left)
                values.append(root.val)
                dfs(root.right)

            return values

        dfs(root)
        closest_val = values[0]
        min_diff = abs(target - values[0])
        for val in values[1:]:
            if abs(target - val) < min_diff:
                min_diff = abs(target - val)
                closest_val = val
                
        return closest_val