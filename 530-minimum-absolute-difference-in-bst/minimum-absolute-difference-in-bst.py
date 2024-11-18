# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def dfs(root):
            if root == None:
                return 
            dfs(root.left)
            values.append(root.val)
            dfs(root.right)

        dfs(root)
        minimum = 100000
        for i in range(0,len(values)-1):
            minimum = min(values[i+1] - values[i],minimum)
        return minimum 