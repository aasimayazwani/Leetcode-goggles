# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        values = []
        forest = []
        def dfs(root):
            if root == None:
                return None

            if (root.left == None) and (root.right == None):
                values.append(root.val)
                return None  
            
            root.left = dfs(root.left)    
            root.right = dfs(root.right)
            
            return root 
        while root:
            root = dfs(root)
            forest.append(values)
            values = []

        return forest 
