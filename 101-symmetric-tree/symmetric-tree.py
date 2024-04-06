# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        current = [root]
        levels = []
        while current:
            values = []
            current_values = []
            for i in range(0,len(current)):
                node = current[i]
                if node.left != None:
                    values.append(node.left)
                    current_values.append(node.left.val)
                if node.left == None:
                    current_values.append("missing")
                if node.right != None:
                    values.append(node.right)
                    current_values.append(node.right.val)
                if node.right == None:
                    current_values.append("missing")
                
            current = values
            #print(current_values)
            if (current_values == current_values[::-1]):
                pass
            else:
                return False
        return True 