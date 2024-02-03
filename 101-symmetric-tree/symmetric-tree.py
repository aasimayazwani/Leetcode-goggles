# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        current = [root]
        while len(current) > 0:
            collection = []
            values = []
            for i in range(0,len(current)):
                node= current[i]
                if node.left != None:
                    collection.append(node.left)
                    values.append(node.left.val)
                if node.left == None:
                    values.append("missing")
                if node.right != None:
                    collection.append(node.right)
                    values.append(node.right.val)
                if node.right == None:
                    values.append("missing")
            current = collection
            if values != values[::-1]:
                return False
        return True 
            
                    