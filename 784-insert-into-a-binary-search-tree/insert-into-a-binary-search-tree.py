# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = root
        if root == None:
            return TreeNode(val)
        
        while current:
            candidates = []
            while True:
                if val > current.val:
                    if current.right == None:
                        current.right = TreeNode(val)
                        return root
                    else:
                        current = current.right
                if val < current.val:
                    if current.left == None:
                        current.left = TreeNode(val)
                        return root
                    else:
                        current = current.left
        return root