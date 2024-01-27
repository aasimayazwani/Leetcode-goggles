# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current = [root]
        while current:
            collections = []
            for i in range(0,len(current)):
                node = current[i]
                if node.val == val:
                    return node
                if node.left != None:
                    collections.append(node.left)
                if node.right != None:
                    collections.append(node.right)
            current = collections 
        return None 