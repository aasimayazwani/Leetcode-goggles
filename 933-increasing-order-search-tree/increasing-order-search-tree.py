# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        ans = []
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        new = TreeNode(ans[0])
        final = new
        for i in range(1,len(ans)):
            succesor = TreeNode(val=ans[i])
            new.right = succesor
            new = new.right 
        return final 
