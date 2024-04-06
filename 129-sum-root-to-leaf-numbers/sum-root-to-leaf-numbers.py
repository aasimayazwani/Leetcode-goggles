# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = []
        def dfs(root,path):
            if root == None:
                return 
            if root.left != None:
                dfs(root.left,path + ">" + str(root.left.val))
            if (root.left == None) and (root.right == None):
                total = path
                value = int("".join(total.split(">")))
                result.append(value)
            if root.right != None:
                dfs(root.right,path + ">" + str(root.right.val))

        dfs(root,str(root.val))
        return sum(result)