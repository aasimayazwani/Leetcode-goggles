# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        current = self.running(root,target)
        return current
        
    def running(self,root,target):
        def dfs(root):
            if root == None:
                return 
            else:
                root.left = dfs(root.left)
                root.right = dfs(root.right)

                if (root.left == None) and (root.right == None) and (root.val == target):
                    return None

                return root
        value = dfs(root)
        return value 
