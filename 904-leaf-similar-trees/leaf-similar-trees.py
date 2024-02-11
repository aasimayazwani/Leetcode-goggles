# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        first = self.explore(root1)
        second =self.explore(root2)
        return first == second
    
    def explore(self,root):
        leafs = []
        def dfs(root):
            if root == None:
                return 

            else:
                dfs(root.left)
                if root.left == None and root.right == None:
                    leafs.append(root.val)
                dfs(root.right)
            return leafs
        return dfs(root)
            
