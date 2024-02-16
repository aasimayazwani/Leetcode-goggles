# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(root,minimum,maximum):
            if root == None:
                return 
            else:
                minimum = min(root.val,minimum)
                maximum = max(root.val,maximum)
                dfs(root.left,minimum,maximum)
                values.append(abs(maximum-minimum))
                dfs(root.right,minimum,maximum)
        dfs(root,10000000,-1)
        #print(values)
        return max(values)