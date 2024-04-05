# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        def backtrack(root,path):
            if root == None:
                return 
            else:
                if root.left != None:
                    backtrack(root.left,path+">" + str(root.left.val))
                if (root.left == None) and (root.right == None):
                    value = int("".join(path.split(">")))
                    result.append(value)
                if root.right != None:
                    backtrack(root.right,path+">" + str(root.right.val))
        
        backtrack(root,str(root.val))
        return sum(result)