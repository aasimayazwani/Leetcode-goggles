# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        result = set()
        def dfs(root):
            if root == None:
                return 
            else:
                result.add(root.val)
                dfs(root.left)
                dfs(root.right)
            return result 
        ans = dfs(root)
        return len(ans)==1 

            