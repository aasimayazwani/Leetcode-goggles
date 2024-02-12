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

            return values

        dfs(root)
        total = 10000000
        for i in range(0,len(values)-1):
            total = min(total,values[i+1]-values[i])

        return total

