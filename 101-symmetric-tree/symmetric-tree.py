# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        current = [root]
        while current:
            child = []
            values = []
            for i in range(0,len(current)):
                node = current[i]
                if node.left:
                    child.append(node.left)
                    values.append(node.left.val)
                if node.left== None:
                    values.append("None")
                if node.right:
                    child.append(node.right)
                    values.append(node.right.val)
                if node.right == None:
                    values.append("None")
            if values != values[::-1]:
                return False
            current = child
        return True