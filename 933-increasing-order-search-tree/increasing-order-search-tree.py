# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root):
            if root == None:
                return 
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        ans = []
        dfs(root)
        result = cur = TreeNode(-1)
        for i in range(0,len(ans)):
            temp = TreeNode(ans[i])
            cur.right = temp
            cur = cur.right
        return result.right 
