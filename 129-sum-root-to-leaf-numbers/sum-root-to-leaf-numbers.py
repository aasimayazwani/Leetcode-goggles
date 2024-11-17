# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]):
        ans = []
        def dfs(root,path):
            if root == None:
                return 
            dfs(root.left,path+str(root.val))
            if root.left == None and root.right == None:
                ans.append(int(path+str(root.val)))
            dfs(root.right,path+str(root.val))
        dfs(root,"")
        return sum(ans)